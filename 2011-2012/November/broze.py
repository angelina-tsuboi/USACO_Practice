## Contest Timing

"""
Problem 1: Contest Timing [Brian Dean]

Bessie the cow is getting bored of the milk production industry, and wants 
to switch to an exciting new career in computing.  To improve her coding
skills, she decides to compete in the on-line USACO competitions.  Since
she notes that the contest starts on November 11, 2011 (11/11/11), she
decides for fun to download the problems and begin coding at exactly 11:11
AM on 11/11/11.

Unfortunately, Bessie's time management ability is quite poor, so she wants
to write a quick program to help her make sure she does not take longer
than the 3 hour (180 minute) time limit for the contest.  Given the date
and time she stops working, please help Bessie compute the total number of
minutes she will have spent on the contest.

PROBLEM NAME: ctiming

INPUT FORMAT:

* Line 1: This line contains 3 space-separated integers, D H M,
        specifying the date and time at which Bessie ends the contest.
        D will be an integer in the range 11..14 telling the day of
        the month; H and M are hours and minutes on a 24-hour clock
        (so they range from H=0,M=0 at midnight up through H=23,M=59
        at 11:59 PM).

SAMPLE INPUT (file ctiming.in):

12 13 14

INPUT DETAILS:

Bessie ends the contest on November 12, at 13:14 (that is, at 1:14 PM).

OUTPUT FORMAT:

* Line 1: The total number of minutes spent by Bessie in the contest,
        or -1 if her ending time is earlier than her starting time.

SAMPLE OUTPUT (file ctiming.out):

1563

OUTPUT DETAILS:

Bessie ends the contest 1563 minutes after she starts.
"""

def findBessieTime(D, H, M):
  #11/11/11 -> 11:11
  amountDayValue = 1440 * (D - 11)
  amountHours = 60 * (H - 11);
  amountMin = M - 11;
  return amountDayValue + amountHours + amountMin;

print(findBessieTime(12,13,14))

"""
Problem 2: Awkward Digits [Brian Dean]

Bessie the cow is just learning how to convert numbers between different
bases, but she keeps making errors since she cannot easily hold a pen
between her two front hooves.  

Whenever Bessie converts a number to a new base and writes down the result,
she always writes one of the digits wrong.  For example, if she converts
the number 14 into binary (i.e., base 2), the correct result should be
"1110", but she might instead write down "0110" or "1111".  Bessie never
accidentally adds or deletes digits, so she might write down a number with
a leading digit of "0" if this is the digit she gets wrong.

Given Bessie's output when converting a number N into base 2 and base 3,
please determine the correct original value of N (in base 10). You can
assume N is at most 1 billion, and that there is a unique solution for N.

Please feel welcome to consult any on-line reference you wish regarding
base-2 and base-3 numbers, if these concepts are new to you.

PROBLEM NAME: digits

INPUT FORMAT:

* Line 1: The base-2 representation of N, with one digit written
        incorrectly.

* Line 2: The base-3 representation of N, with one digit written
        incorrectly.

SAMPLE INPUT (file digits.in):

1010
212

INPUT DETAILS:

When Bessie incorrectly converts N into base 2, she writes down
"1010".  When she incorrectly converts N into base 3, she writes down "212".

OUTPUT FORMAT:

* Line 1: The correct value of N.

SAMPLE OUTPUT (file digits.out):

14

OUTPUT DETAILS:

The correct value of N is 14 ("1110" in base 2, "112" in base 3).
"""

"""
Problem 3: Moo Sick [Rob Seay]

Everyone knows that cows love to listen to all forms of music.  Almost all
forms, that is -- the great cow composer Wolfgang Amadeus Moozart
once discovered that a specific chord tends to make cows rather ill.  This
chord, known as the ruminant seventh chord, is therefore typically avoided
in all cow musical compositions.

Farmer John, not knowing the finer points of cow musical history, decides
to play his favorite song over the loudspeakers in the barn.  Your task is
to identify all the ruminant seventh chords in this song, to estimate how
sick it will make the cows.

The song played by FJ is a series of N (1 <= N <= 20,000) notes, each an
integer in the range 1..88.  A ruminant seventh chord is specified by a
sequence of C (1 <= C <= 10) distinct notes, also integers in the range
1..88.  However, even if these notes are transposed (increased or decreased
by a common amount), or re-ordered, the chord remains a ruminant seventh
chord!  For example, if "4 6 7" is a ruminant seventh chord, then "3 5 6"
(transposed by -1), "6 8 9" (transposed by +2), "6 4 7" (re-ordered), and
"5 3 6" (transposed and re-ordered) are also ruminant seventh chords.

A ruminant seventh chord is a sequence of C consecutive notes satisfying
the above criteria. It is therefore uniquely determined by its starting
location in the song. Please determine the indices of the starting
locations of all of the ruminant seventh chords.

PROBLEM NAME: moosick

INPUT FORMAT:

* Line 1: A single integer: N.

* Lines 2..1+N: The N notes in FJ's song, one note per line.

* Line 2+N: A single integer: C.

* Lines 3+N..2+N+C: The C notes in an example of a ruminant seventh
        chord.  All transpositions and/or re-orderings of these notes
        are also ruminant seventh chords.

SAMPLE INPUT (file moosick.in):

6
1
8
5
7
9
10
3
4
6
7

INPUT DETAILS:

FJ's song is 1,8,5,7,9,10.  A ruminant seventh chord is some
transposition/re-ordering of 4,6,7.

OUTPUT FORMAT:

* Line 1: A count, K, of the number of ruminant seventh chords that
        appear in FJ's song.  Observe that different instances of
        ruminant seventh chords can overlap each-other.

* Lines 2..1+K: Each line specifies the starting index of a ruminant
        seventh chord (index 1 is the first note in FJ's song, index N
        is the last).  Indices should be listed in increasing sorted
        order.

SAMPLE OUTPUT (file moosick.out):

2
2
4

OUTPUT DETAILS:

Two ruminant seventh chords appear in FJ's song (and these occurrences
actually overlap by one note).  The first is 8,5,7 (transposed by +1 and
reordered) starting at index 2, and the second is 7,9,10 (transposed by +3)
starting at index 4.
"""

"""
Problem 4: Cow Beauty Pageant (Bronze Level) [Brian Dean]

Hearing that the latest fashion trend was cows with two spots on their
hides, Farmer John has purchased an entire herd of two-spot cows. 
Unfortunately, fashion trends tend to change quickly, and the most popular
current fashion is cows with only one spot!  

FJ wants to make his herd more fashionable by painting each of his cows in
such a way that merges their two spots into one.  The hide of a cow is
represented by an N by M (1 <= N,M <= 50) grid of characters like this:

................
..XXXX....XXX...
...XXXX....XX...
.XXXX......XXX..
........XXXXX...
.........XXX....

Here, each 'X' denotes part of a spot.  Two 'X's belong to the same spot if
they are vertically or horizontally adjacent (diagonally adjacent does not
count), so the figure above has exactly two spots.  All of the cows in FJ's
herd have exactly two spots.

FJ wants to use as little paint as possible to merge the two spots into
one.  In the example above, he can do this by painting only three
additional characters with 'X's (the new characters are marked with '*'s
below to make them easier to see).

................
..XXXX....XXX...
...XXXX*...XX...
.XXXX..**..XXX..
........XXXXX...
.........XXX....

Please help FJ determine the minimum number of new 'X's he must paint in
order to merge two spots into one large spot.

PROBLEM NAME: pageant

INPUT FORMAT:

* Line 1: Two space-separated integers, N and M.

* Lines 2..1+N: Each line contains a length-M string of 'X's and '.'s
        specifying one row of the cow hide pattern.

SAMPLE INPUT (file pageant.in):

6 16
................
..XXXX....XXX...
...XXXX....XX...
.XXXX......XXX..
........XXXXX...
.........XXX....

INPUT DETAILS:

The pattern in the input shows a cow hide with two distinct spots, labeled
1 and 2 below:

................
..1111....222...
...1111....22...
.1111......222..
........22222...
.........222....

OUTPUT FORMAT:

* Line 1: The minimum number of new 'X's that must be added to the
        input pattern in order to obtain one single spot.

SAMPLE OUTPUT (file pageant.out):

3

OUTPUT DETAILS:

Three 'X's suffice to join the two spots into one:

................
..1111....222...
...1111X...22...
.1111..XX..222..
........22222...
.........222....
"""
