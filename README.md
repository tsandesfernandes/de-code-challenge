# coding challenge 
challenge to parse  Common Crawl data  to nosql db and then find commom values and send to rdbms

## tech stack

* python
* postgres
* aws dynamodb
* aws s3

## Steps

* created a iam user and gave programmatic permission
* set up a dynamodb table running `create_dynamo_table.py`
* initially I tried to read the data source file straight from s3 throwing 400
* then I made a different approach and downloaded one of the files locally running `download_parque_file.sh`
* tried to parse the whole file causing memory problems locally
* changed to parse the file in batches, where in this examples I only upload the first 10 records to dynamodb from `read_chunk.py`
* once the records were in dynamodb, I pulled a postgres docker image locally 
* create an example table running `create_table_postgres.sql` in psql command line
* executed `insert_db_py` to insert a record into postgres