# Background

`git` seems like magic in its ability to merge two (or more) different
sets of code.  But it's really just taking changes and applying them
because different people were editing different parts of the code.  It
**still doesn't understand the code** though.  It can't fix
fundamental differences in two people making two different changes
that are incompatible, **but in different parts of a file**.

# Example

In this repository, there are 4 points of code that you should look
at.  They're each given a tag that you can checkout to look at the
simple code.  I used python since everyone should understand it.

* run `git checkout initial`: you'll see a `test.py` file where a very
  simple function `print_greeting` is defined that simply prints
  *"hello"* followed by something passed in.
  
* next `git checkout change1`: Let's consider the case where one
  person has modified the code to have `print_greeting` taken an
  argument to introduce themselves as they print the greeting.  They
  properly did this in the `say-who-is-greeting` branch.
  
* next see `git checkout change2`: someone else started a branch
  (`hello-all-planets`) with their own awesome new idea to say hello
  to all the planets.

  [Note: after a large dispute with team mates about whether *pluto*
  was a planet or not, the *not* members won because that's what
  current scientists think.]

* Finally, in `git checkout merged`: a third person is responsible for
  merging everyone's changes together and did so by running:
  
    1. git checkout main
    2. git merge say-who-is-greeting
    3. git merge hello-all-planets
    
  Yay, done right!  **Note: there were no conflicts**.  The code
  merged just fine, but does it work?  No.  It's up to the person that
  is managing the main or other combining branch to ensure that the
  APIs themselves haven't changed in an incompatible way.  If the
  `hello-all-planets` branch was merged second, it would need to be
  fixed first before merging rather than merging unconditionally and
  hoping that `git` would have flagged all problems.
  
  `git` can't flag all problems: it doesn't understand what the code
  is actually doing or how it works.
  
Note that ensuring a test case was run before a commit or merge was
allowed to happen would have caught this problem.  Because the test
case would have shown that the second merge (`hello-all-planets`)
would have not allowed the code to actually run.  In this case, even
had the final merger actually run "test.py" after merging they would
have noticed the problem (and hopefully hadn't pushed the merge to
github yet).
