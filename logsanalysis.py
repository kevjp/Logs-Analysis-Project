#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Thu Jul 20 12:50:52 2017

@author: kevinryan



Provide analysis of news database
    - Top 3 accessed articles see function top3articles
    - List of most accessed authors see function mostpopularauthors
    - List of days when greater than 1% of requests lead to errors see function
      days_1percenterrors
"""

import psycopg2
import datetime


class News(object):
    # Initialise db connection, generate cursor and create any views

    def __init__(self):

        pg = psycopg2.connect("dbname = news")
        self.cursor = pg.cursor()
        # Create view will be used by question 1 and 2 - view relates to join
        # between log and articles table
        self.cursor.execute(
            """CREATE VIEW log_article_join AS SELECT path, title, author
            FROM log, articles WHERE path = CONCAT('/article/', slug)""")
        with open('results.txt', 'w') as results_file:
            # Provide date script is run in results file
            line = str(datetime.datetime.today().strftime('%Y-%m-%d')) + "\n"
            results_file.write(line)

    def top3articles(self):

        # Select top 3 article titles in news db
        self.cursor.execute(
            """SELECT title, COUNT(path) as count FROM log_article_join
            GROUP BY title ORDER BY count DESC LIMIT 3""")

        top_articles = self.cursor.fetchall()

        # Write result of select statment to results file
        with open('results.txt', 'a') as results_file:
            results_file.write("The top 3 articles in descending order are:\n")

            for title, count in top_articles:
                line = title + " - " + str(count) + "\n"
                results_file.write(line)

    def mostpopularauthors(self):

        # Generate a list of most accessed authors in descending order
        self.cursor.execute(
            """SELECT name, COUNT(name) AS count FROM authors, log_article_join
            WHERE authors.id = author GROUP BY name ORDER BY count DESC;""")

        author_popularity = self.cursor.fetchall()

        # Write result of select statment to results file
        with open('results.txt', 'a') as results_file:
            results_file.write(
                "\n\nThe most popular article authors of all time are:\n")

            for author, count in author_popularity:
                line = author + " - " + str(count) + " views.\n"
                results_file.write(line)

    def days_1percenterrors(self):

        # List of days when greater than 1% of requests lead to errors. Generate
        # the date in month, day, year format along with percentage value.
        self.cursor.execute("""SELECT to_char(day, 'Month DD, YYYY') "day",
            ROUND(percent_total, 1) FROM (SELECT date_trunc('day', time) "day",
            ((SUM(CASE WHEN status != '200 OK' THEN 1 ELSE 0 END) * 100)::
            decimal/COUNT(status)) AS percent_total FROM log GROUP BY day
            ORDER BY percent_total DESC) AS percentage
            WHERE percent_total > 1""")

        error_dates = self.cursor.fetchall()

        # Write result of select statment to results file
        with open('results.txt', 'a') as results_file:
            results_file.write("\n\nOn the following days greater than 1% of "
                               "requests lead to errors:\n")

            for day, percentage in error_dates:
                line = day + " - " + str(percentage) + "% errors" "\n"
                results_file.write(line)

    # Runs functions for script in specific order when run as source file
    def run_functions(self):
        self.top3articles()
        self.mostpopularauthors()
        self.days_1percenterrors()


if __name__ == '__main__':
    # Instantiate the class News
    news = News()
    # Run functions associated with News class
    news.run_functions()
