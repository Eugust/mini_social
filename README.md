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
 Send requests you can here: [Graphql playground](http://127.0.0.1:8000/playground/)
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
#### Requests for post
 Create
 ```
 mutation {
  createPost(
    postData: {
			text: "Some test post4"
    }
  ) {
    post {
      id
      text
      author {
        id
        username
      }
      pubDate
    }
  }
}
 ```
 Update
 ```
 mutation {
  updatePost (
    id: 2,
    text: "update test post"
  ) {
    post {
      id
      text
    }
  }
}
 ```
 Delete
 ```
 mutation {
  deletePost (
    id: 2
  ) {
    post {
      id
    }
  }
}
 ```
#### Requests for comment
 Create
 ```
 mutation {
  createComment(
    commentData: {
      text: "nice comment bro2"
      post: { id: 1 }
    }
  ) {
    comment {
      id
      text
      post {
        id
      }
      author {
        username
      }
    }
  }
}
 ```
#### Requests like post and comment
 Like post
 ```
 mutation {
  likePost (
    id: 4
  ) {
    post {
      id
      text
      pubDate
      author{
        username
      }
      likes
    }
  }
}
 ```
 Like comment
 ```
 mutation {
  likeComment (
    id: 5
  ) {
    comment {
      id
      text
      created
      author {
        username
      }
      likes
    }
  }
}
 ```
