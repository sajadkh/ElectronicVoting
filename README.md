# Electronic voting

## installation
~~~
git clone https://github.com/sajadkh/ElectronicVoting.git
~~~

~~~
pip install -r requirements.txt
~~~

~~~
python manage.py migrate
~~~

~~~
python manage.py runserver
~~~

## APIs List

### Election
#### URL
~~~
http://{{serverUrl}}/election
~~~

#### GET
Get Elections List Or Get Elections Details

##### input
~~~
{
    id: "integer" // code of election not required
}
~~~

##### response
~~~
[
    {
        "id": 1,
        "Title": "test1"
    },
    {
        "id": 2,
        "Title": "test2"
    },
    {
        "id": 3,
        "Title": "test3"
    }
]
~~~


#### POST

Add Election

input
~~~
{
	"Title": "string", // title of election
	"Start_Time": "string", //start time of election yyyy-mm-dd 
	"End_Time": "string", //end time of election yyyy-mm-dd
	"ListOfChoices": ["string"] // list of choices
}
~~~
response
~~~
{}
~~~

#### PUT

Edit Election

input

~~~
{
    "id": "integer", // id of election
	"Title": "string", // title of election not required
	"Start_Time": "string", //start time of election yyyy-mm-dd not required 
	"End_Time": "string", //end time of election yyyy-mm-dd not required
	"ListOfChoices": ["string"] // list of choices not required
}
~~~

response
~~~
{}
~~~

#### DELETE

Delete Election

input
~~~
{
    id: "integer" // code of election
}
~~~

response
~~~
{}
~~~

### Vote
#### URL
~~~
http://{{serverUrl}}/vote
~~~

#### PUT
Vote To Election

input
~~~
{
    id: "integer" // code of election
}
~~~

response

~~~
{}
~~~

### Choices
#### URL
~~~
http://{{serverUrl}}/choices
~~~

#### GET
Get Choices List Of Election

input
~~~
{
    id: "integer" // code of election
}
~~~

response

~~~
[
    "choice1",
    "choice2"
]
~~~

### ElectionExist
#### URL
~~~
http://{{serverUrl}}/existElection
~~~

#### GET
Check Is Election Exist?

input
~~~
{
    id: "integer" // code of election
}
~~~

response

~~~
{}
~~~