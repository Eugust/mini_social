# mini_social
 Backend for mini social network
## Users capability:
 > Create, delete, update and read posts  
 > Create, delete, update and read comment for post  
 > Like posts or comments
## Tools
 > Django  
 > GraphQL
## Instruction
 Clone this repository
 ```
 git clone 
 ```
 Install pipenv (if you don't have)
 ```
 pip install --user pipx
 pipx install pipenv
 ```
 Run server with pipenv
 ```
 pipenv run python manage.py runserver
 ```
## API
#### Get all posts
 Request:
 ```
 query {
  allPosts(first:10) {
    id
    text
    pubDate
    author{
      username
    }
    likes
  }
}
 ```
 Response:
 ```
 {
  "data": {
    "allPosts": [
      {
        "id": "4",
        "text": "Some test post",
        "pubDate": "2022-01-24T04:52:48.682562+00:00",
        "author": {
          "username": "test_user2"
        },
        "likes": 1
      },
    ...
  }
 }
 ```
#### Get all comments of post
 ```
 query {
  allCommentsPost(postId:1, first:9) {
    id
    text
    created
    author{
      username
    }
    likes
  }
}
 ```
#### Create User
 ```
 mutation {
  createUser (
    userData: {
      username: "test_user2",
      password: "someEsxtraPAss",
      firstName: "User",
      lastName: "User",
      phone: "+11111112",
      gender: "M"
    }
  ) {
    user {
      id
      username
      firstName
      lastName
      phone
      gender
    }
    token
  }
}
 ```
#### For CRUD post and CRUD comment you need token  
 Use token in HTTP HEADERS:
 ```
 {
  "authorization": token
}
 ```
