# Table of Contents

[Logs-Analysis-Project](#logs-analysis-project)

[Requirements](#requirements)

[Install](#install)

[Views](#views)

[Examples of use](#examples-of-use)

[Contributing](#contributing)

[License](#license)


## Logs-Analysis-Project
Logs Analysis Project generated as part of Full Stack Udacity Nanodegree. Provides information regarding news database including:
 * The top 3 accessed articles see function top3articles
 * A list of most accessed authors see function mostpopularauthors
 * A List of days when greater than 1% of requests lead to errors see function days_1percenterrors

## Requirements
Requires python 2.7 to be installed

Requires the following python modules to be installed:
 * psycopg2
 * datetime
 
 Also requires access to news database. Contact kevin@ryancodingdesign.com for access.


## Install
Install the following python file by cloing the Logs-Analysis-Project repository on to your local system

`$ git clone https://github.com/kevjp/Logs-Analysis-Project.git`

## Views

The python script logsanalysis.py generates the Postgresql view log_article_join which is a join between the log table and the articles table using the query:
`CREATE VIEW log_article_join AS SELECT path, title, author
            FROM log, articles WHERE path = CONCAT('/article/', slug)`

## Examples of use

`$ python logsanalysis.py`

## Contributing
Please feel free to contribute to the Logs-Analysis-Project. You can raise issues and issue pull requests. I will attempt to respond to outstanding requests as soon as possible.

## License

The contents of this repository are covered under the [MIT License](https://choosealicense.com/licenses/mit/#)

