# Employee #1 Speech Synthesizer

Craig Cannon has an interesting series of interviews called [Employee #1](http://blog.ycombinator.com/category/employee-1/).

I put together this little python script so I can listen to them as podcasts
while I'm in the car or doing things around the house.

## Usage

### Clone repo

```
$ git clone git@github.com:Olshansk/employee_number_one_audio.git
$ cd employee_number_one_audio
$ pip install -r requirment.txt
```

### Synthesize

Pass in the link to the interview as an argument to the script:

```
$ python first_employee_to_sound.py http://blog.ycombinator.com/employee-1-amazon/
```

## Profiling

The Amazon interview linked above took about 30 seconds to synthesize on my 2012
Macbook Pro.

## Other

This python script probably only works on a mac because it utilizes macOS's
`say` command.
