KOA Backend Developer Task
==============
![CI Workflow](https://github.com/dennismwagiru/koa/actions/workflows/checks.yml/badge.svg "Workflow Badge")

### Background
Create a Django application with an API that receives a set of points on a grid as semicolon separated values. And then it finds the points that are closest to each other. Store the received set of points and the closest points on a DB.

An example input would look like this:
2,2;-1,30;20,11;4,5

And then in this case the result would be:
2,2;4,5

Additionally, please add an admin interface for viewing values stored on the DB. And add unit tests where it makes sense.

### Requirements
* Git is required to clone the application. Else you can download as a zip file, extract it and proceed with step 2
* This application is configured to run on *Docker*. It should therefore be preinstalled

  | Service    | Port |
  |------------|------|
  | APP (HTTP) | 8000 |
  | Postgresql | 5432 |

### Running Locally
1. Clone the repository
    ```bash
    git clone git@github.com:dennismwagiru/koa.git && cd koa
    ```

2. Build and start server
    ```bash
       make install
    ```
   Navigate to <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> to test the end-point


3. Post Grid
    ```bash
       curl --location 'http://127.0.0.1:8000/api/grid/' \
       --header 'Content-Type: application/json' \
       --data '{
       "points": "2,2;-1,30;4,5;6,6;6,7"
       }'
    ```

### Other scripts included
* Subsequent runs
    ````bash
        make up
    ````
* Build docker image
    ````bash
        make build
    ````
* Run migrations
    ````bash
        make migrate
    ````
* Create superuser
    ````bash
        make superuser
    ````
* Run tests
    ````bash
        make test
    ````
* Check Linting
    ````bash
        make lint
    ````
* Open app bin bash
    ````bash
        make app-bin
    ````