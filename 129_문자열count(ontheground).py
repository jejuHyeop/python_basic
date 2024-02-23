# Rose On the ground   에서 한번만 사용된 단어는?
a='''My life's been magic, seems fantastic
I used to have a hole in the wall with a mattress
Funny when you want it, suddenly you have it
You find out that your gold's just plastic
Every day, every night
I've been thinkin' back on you and I
Every day, every night
I worked my whole life
Just to get right, just to be like
"Look at me, I'm never coming down"
I worked my whole life
Just to get high, just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
(Yeah, what goes up must come down)
(Nah, but they don't hear me though)
(You're runnin' out of time)
My world's been hectic, seems electric
But I've been waking up with your voice in my head
And I'm tryna send a message and let you know that
Every single minute I'm without you, I regret it
Every day, every night
I've been thinkin' back on you and I
Every day, every night
I worked my whole life
Just to get right, just to be like
"Look at me, I'm never coming down"
I worked my whole life
Just to get high, just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
(Yeah, what goes up must come down)
(Nah, but they don't hear me though)
(You're runnin' out of time)
I'm way up in the clouds
And they say I've made it now
But I figured it out
Everything I need is on the ground (yeah, yeah)
Just drove by your house (just drove by your house)
So far from you now (so far from you now)
But I figured it out
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
On the ground
(Nah, but they don't hear me though)
Everything I need is on the ground'''

for i in ",!()":
    a = a.replace(i, " ")
a = a.replace("n't", " not ")
a = a.replace("n'", "ng")
a = a.replace("'m", " am ")
a = a.replace("'ve", " have ")
a = a.replace("'re", " are ")
a = a.replace("'s", " is ")
a = a.lower()

단어들 = a.split()

li = []
for i in 단어들:
    if 단어들.count(i) == 1:
        li.append(i)
print(li)