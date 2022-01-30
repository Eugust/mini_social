# mini_social
 Backend for mini social network
## Users capability:
 > Create, delete, update and read posts  
 > Create, delete, update and read comment for post  
 > Like posts or comments
## Tools
 > Django  
 > GraphQL  
 > GrapgQL playground
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
