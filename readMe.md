<h1>Movie Management System</h1>
<h4 style="text-align: right;">Term project for CS521</h4>
<h5 style="text-align: right;">Author: Selina Liu</h5>

<p>This program allow people to register as a user for the website, user could view , update rate and add reviews the  movies. Admins could
add/delete movies. The program will display the movies according to their rating in descending order. </p>
<hr>
<h2>Features</h2>
<ul>
<li>sign up as the new user</li>
<li>return user sign in</li>
<li>add new movie(admin only)</li>
<li>delete the movie(admin only)</li>
<li>add review(login user only)</li>
<li>update rate(login user only)</li>
<li>Get movie by id</li>
<li>display all movies based on rating </li>

</ul>

<h2> Design</h2>
<ul>
<li>Main: run main.py to execute this program</li>
<li>Models</li>
    <ul>
        <li>Movie class: id, name,release_date, reviews, rate, rated_people</li>
        <li>User class: id,email,username,password,isAdmin</li>
    </ul>
<li>Management</li>
    <ul>
    <li>Movie_management:add/delete movies, add review and update rating</li>
    <li>User_management:sign up/log in, add user, check login status</li>
    </ul>
<li>Exceptions: extend exception class, make it more related to our program</li>
    <ul>
    <li>RegistrationError: related to registration issues</li>
    <li>AuthenticationError: related to authentication issues</li>
    <li>MovieNotFoundError: when ask movie is not found</li>
    <li>InvalidInputError: reminder user input invalid command</li>
    </ul>
<li>Test: unit test for methods in management</li>


</ul>


<h2> Requirements Match</h2>
<ul>
<li>Dictionary:users, email as key, users as value, movies, id as key, movie as value</li>
<li>List Usage: review list, also when we sort movies, we extract values from dictionary, and sort in list
<li>Tuple: admins, this use for store admins, admins accounts are immutable</li>
<li>Set:user_emails, for quickly check if the user has registered or not</li>
<li>For loop: when we display the movie in index</li>
<li>Conditional statements: very common in this program</li>
<li>Try Block: when add/delete movies or verify inputs, very common</li>
<li>User Defined class: User class,Movie class, and their management class, all those classes should match all the requirements.
<li>Unit Tests: in test package, we test all functions for management class</li>
<li>Run Successfully: I have tested both happy cases and failed cases, they all run successfully</li>
</ul>

<h2> Test cases</h2>
<h4>Happy path</h4>
<ul>
<li>register as a new user use correct format</li>
<li>login successfully</li>
<li>add a movie when login as an admin with valid input</li>
<li>delete a movie when login as an admin</li>
<li>update rating when login</li>
<li>add a new review when login</li>
<li>display all the movies based on rating</li>
</ul>

<h4> Failed Path</h4>
<ul>
    <li>register a new account use exist user email, excepted RegistrationError</li>
    <li>use a new email to login,excepted AuthenticationError</li>
    <li>input the wrong password,excepted AuthenticationError</li>
    <li>use non admin account to add/delete movie, excepted AuthenticationError</li>
    <li>add review without login, excepted AuthenticationError</li>
    <li> when add review, input the wrong movie id, excepted InvalidInputError</li>
    <li>update rating without login, excepted AuthenticationError</li>
    <li>input a command that is not in our menu, remind user to input valid command</li>
    <li>try to modify a non-exist movie, excepted MovieNotFoundError</li>
    <li>when register as a new user,input email does not have"@",excepted InvalidInputError</li>
    <li>password is less than 5 chars,excepted InvalidInputError </li>
    <li>username is empty,excepted InvalidInputError</li>
    <li>when add a movie, the movie name is empty or the description is empty, excepted InvalidInputError</li>
    <li>when add a movie, the rate is not a number or not in range 0-10, excepted InvalidInputError</li>
    <li>when add a movie, the release_date is not number range from 1900-2024, excepted InvalidInputError</li>
</ul>


