# Generated by Django 3.2.4 on 2021-06-23 21:55

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0076_preview_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name="author",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="bookwyrm_au_search__b050a8_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="book",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="bookwyrm_bo_search__51beb3_gin"
            ),
        ),
        migrations.RunSQL(
            sql="""
                CREATE FUNCTION book_trigger() RETURNS trigger AS $$
                begin
                    new.search_vector :=
                        coalesce(
                            NULLIF(setweight(to_tsvector('english', coalesce(new.title, '')), 'A'), ''),
                            setweight(to_tsvector('simple', coalesce(new.title, '')), 'A')
                        ) ||
                        setweight(to_tsvector('english', coalesce(new.subtitle, '')), 'B') ||
                        (SELECT setweight(to_tsvector('simple', coalesce(array_to_string(array_agg(bookwyrm_author.name), ' '), '')), 'C')
                            FROM bookwyrm_book
                            LEFT OUTER JOIN bookwyrm_book_authors
                            ON bookwyrm_book.id = bookwyrm_book_authors.book_id
                            LEFT OUTER JOIN bookwyrm_author
                            ON bookwyrm_book_authors.author_id = bookwyrm_author.id
                            WHERE bookwyrm_book.id = new.id
                        ) ||
                        setweight(to_tsvector('english', coalesce(new.series, '')), 'D');
                    return new;
                end
                $$ LANGUAGE plpgsql;

                CREATE TRIGGER search_vector_trigger
                BEFORE INSERT OR UPDATE OF title, subtitle, series, search_vector
                ON bookwyrm_book
                FOR EACH ROW EXECUTE FUNCTION book_trigger();

                UPDATE bookwyrm_book SET search_vector = NULL;
            """,
            reverse_sql="""
                DROP TRIGGER IF EXISTS search_vector_trigger
                ON bookwyrm_book;
                DROP FUNCTION IF EXISTS book_trigger;
            """,
        ),
        # when an author is edited
        migrations.RunSQL(
            sql="""
                CREATE FUNCTION author_trigger() RETURNS trigger AS $$
                begin
                    WITH book AS (
                        SELECT bookwyrm_book.id as row_id
                        FROM bookwyrm_author
                        LEFT OUTER JOIN bookwyrm_book_authors
                        ON bookwyrm_book_authors.id = new.id
                        LEFT OUTER JOIN bookwyrm_book
                        ON bookwyrm_book.id = bookwyrm_book_authors.book_id
                    )
                    UPDATE bookwyrm_book SET search_vector = ''
                    FROM book
                    WHERE id = book.row_id;
                    return new;
                end
                $$ LANGUAGE plpgsql;

                CREATE TRIGGER author_search_vector_trigger
                AFTER UPDATE OF name
                ON bookwyrm_author
                FOR EACH ROW EXECUTE FUNCTION author_trigger();
            """,
            reverse_sql="""
                DROP TRIGGER IF EXISTS author_search_vector_trigger
                ON bookwyrm_author;
                DROP FUNCTION IF EXISTS author_trigger;
            """,
        ),
        # when an author is added to or removed from a book
        migrations.RunSQL(
            sql="""
                CREATE FUNCTION book_authors_trigger() RETURNS trigger AS $$
                begin
                    UPDATE bookwyrm_book SET search_vector = ''
                    WHERE id = coalesce(new.book_id, old.book_id);
                    return new;
                end
                $$ LANGUAGE plpgsql;

                CREATE TRIGGER book_authors_search_vector_trigger
                AFTER INSERT OR DELETE
                ON bookwyrm_book_authors
                FOR EACH ROW EXECUTE FUNCTION book_authors_trigger();
            """,
            reverse_sql="""
                DROP TRIGGER IF EXISTS book_authors_search_vector_trigger
                ON bookwyrm_book_authors;
                DROP FUNCTION IF EXISTS book_authors_trigger;
            """,
        ),
    ]
