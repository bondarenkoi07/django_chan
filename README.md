# Django 1337chan

A simple `Django` imageboard project, based on simple manual CMS, that implements the life cycle of threads,
CRUD onto posts (`Comments` model in app) and that uses   django templates on the frontend.  Also there is  searcher above site.

# Structure
Main app `learning` ~~to rule them all~~ consist main settings and urls responsive for routing.  
App `hello_world` contains main logic of imageboard's functionalities.  
App `utils` contains searcher implementation.  

# Models 
Leetchan has units which, according to the idea, shall sort threads by common topic.Threads, in its turn, shall sort comments py specific topic.  
That means `Thread` has foreign key on `Unit` and `Comment` has foreign key on `Thread`.

# Simple setup
You should clone this repo and then enter command below in project's directory:
```bash 
  docker-compose -f docker-compose.yml up -d --build
```
