<div align="center">
<a href="https://flask.palletsprojects.com/en/2.0.x/"><img src="https://blog.paperspace.com/content/images/2019/11/flasklogo.jpg" alt="Flask Python web framework" width="150px"></a>
<a href="https://jwt.io/"><img src="http://jwt.io/img/logo-asset.svg" alt="JWT" width="150px"></a>
</div>

<!-- start jina-description -->

This is a flask service that handles user login and register functions from clinets and returns JWT Token.


<!-- end jina-description -->

# How to use 

This project needs 3rd party packages you can install them by running this command
```bash
pip install -r requirements.txt
```
## Database init

First of all you need to initalize the database, i have used SQLite but you can change from config.py file to any db you want

```bash
flask db init
```

For migrations run:

```bash
flask db migrate
```

Finally update the db 

```bash
flask db upgrade
```

Thats it db is ready. If you want to change User Model, run migration and upgrade after modification you did.


# Get Started

To run server 

```bash
flask run
```

To run server in your LAN

```bash
flask run --host=0.0.0.0
```

# API endpoints

## GET
`localhost:8080 or your custom url` [/api/auth/users](#get-apiauthusers) <br/>

## POST
`localhost:8080 or your custom url` [/api/auth/login](#post-apiauthlogin) <br/>
`localhost:8080 or your custom url` [/api/auth/register](#post-apiauthregister) <br/>

---

### GET /api/auth/users

Returns list of registered users

**Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                         |
| -------------:|:--------:|:-------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `Authentication` | required | JWT  |  This enpoint jwt_protected  
needs a valid jwt authentication header 
|

**Response**

```
[
    {
        "avatar": string,
        "email": string,
        "id": integer,
        "role": string,
        "username": string
    }
]
```
___

### POST /api/auth/login
Request to login endpoint returns JWT

**Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                         |
| -------------:|:--------:|:-------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `email` | required | string  | Email |
|    `password` | required | string  | Password|

**Response**

```
{
    "acces_token": JWT
}
```
___

### POST /api/auth/register
Register user to the system

**Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                         |
| -------------:|:--------:|:-------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `email` | required | string  | Email |
|    `password` | required | string  | Password|
|    `password_check` | required | string  | Password Check|

**Response**

```
{
    "acces_token": JWT
}
```
___