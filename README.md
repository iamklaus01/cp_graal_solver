### Description


### Installation
- Clone the GitHub repository.

    - `git clone https://github.com/iamklaus01/cp_graal_solver.git` <br>
    - `cd cp_graal_solver`

- Install all packages required findable in requirements.txt file
- > `pip install -r requirements.txt`
- Copy the .env file and setup all required field
- > `cp .env.example .env`
- Create pgsql database named graal_solver
- Update this line in `database.py` file `DATABASE_URL = "postgresql://{username}:{password}@localhost/graal_solver"`

### Usage

- Activate your environment if you're using one 
- Start graal solver app
- > `uvicorn main:app --reload`
- Go to http://127.0.0.1:8000/docs for interact with the api without frontend side


### License
All rights reserved.
