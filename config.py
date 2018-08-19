#!/usr/bin/env python
# Hypnotic Spiral
# Copyright (C) 2006, 2007 by Yonah Arakoslav
# yonah.arakoslav@yahoo.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

def prompt(text): return ["!prompt(%r)" % text]
def speak(text): return ["!speak(%r)" % text]
def words_on(): return ["!words_on()"]
def spiral_on(): return ["!spiral_on()"]
def words_off(): return ["!words_off()"]
def spiral_off(): return ["!spiral_off()"]
def pause_music(): return ["!pause_music()"]
def stop_music(): return ["!stop_music()"]
def unpause_music(): return ["!unpause_music()"]
def with_images(lst): return ["!images_on()"] + lst + ["!images_off()"]
def images_on(): return ["!images_on()"]
def images_off(): return ["!images_off()"]
def question(q,var): return ["!open_question(%r,%r)" % (q,var)]
def question_yn(q,y,n): return ["!yn_question(%r,%r,%r)" % (q,y,n)]
def say(text):
    return ["!pause_music()",
            "!speak(%r)" % text,
            "!unpause_music()"]
def cond(q,yes=[],no=[]): return ["!conditional(%r,%s,%s)" % (q,yes,no)]
def question_once(q,var):
    return ["!conditional('\"var\" not in self.variables'," + \
            "[\"!open_question('%s','%s')\"])" % (q,var)]
def jump(dest): return ['!new_text(%r)' % dest]
def words(t): return t.split()


class Standard (object):
    name="Standard"
    description="""\
    This is the standard, basic configuration.  It defines
    everything you should need to use the program.  Most other configurations
    should inherit from it and over-ride the parts they want to change.  A bit
    of the text is inspired by Tabico's Balphagor.  It roughly assumes a
    female submitting to a male, but that either might use this program."""
    broken_fonts = False
    scale = 10
    size = (640, 480)
    time_scale = 2
    frame_rate=60
    fullscreen = False
    color = 255, 255, 255
    alpha = 127
    minimum_delay = 0
    maximum_delay = 0
    text_color = 0, 51, 204
    text_alpha = 254
    shuffle_images = True
    frequencies = { 'spiral' : 1,
                    'images' : 10,
                    'words'  : 20 }
    music = None # Name an MP3 file here, like "music.mp3"
    image_dir = "images/" # Name a directory here, like "images/"
    image_alpha = 255
    def nothing(self): return [ " " ] # for the ending, just spiral and images
    def body(self): return \
        words("Down into trance. Watch the") + \
        spiral_on() + \
        words("""spiral. Hear the program. This program tells you the truth.
        Listen to the program. Let this program program you. $master is a
        Master. $name is a Slave. It is sexy to""") + \
        with_images(words("""see $name changed. $name likes being changed.
        $master changes $name. $master programs $name. $master helps Things
        change $name.""")) + \
        words("""Watch the spiral. The spiral is sexy. The spiral is smooth.
        Over and over. Over and over. So smooth. So pretty. Over and over.
        $name's desires are unformed and simple.""") + \
        with_images(words("""$master's pleasure is deep and rich. $master's
        pleasure is more sexy. $master's pleasure is more important.
        $master's pleasure is more important than $name's pleasure.
        $master is more important than $name.""")) + \
        words("""$name must change her desires to reflect $master's pleasure.
        $name should start to doubt her desires. $name will start to doubt her
        desires. $name will bend her desires to become $master's desires.
        The program tells you what is sexy. The program turns you on.
        $master is a master. This excites you both. $name is a Slave. This
        excites you both. $name will be Changed. This is sexy. This program
        will change $name. It will show you""") + \
        with_images(words("""pictures of Change. $name can Change like this.
        Watch and learn. Watch and see what can be. Watch and see what Change
        is like.""")) + \
        words("""The pictures are sexy. The pictures give you ideas. You
        need the pictures.""") + \
        cond("self.draw_image",
             words("Turn on the pictures.  Hit the 'i' key.")) + \
        words("""You lust for the pictures. $name will be like the
        pictures. This turns you both on. You need the changes. You
        lust for the changes. $name will be changed. This is sexy. It
        would feel so good just to surrender to it.""") + \
        cond("not self.config.fullscreen",
             words("Feel so good to go fullscreen.  Hit 'f'."),
             words("So good to be fullscreen.  So good to be immersed.")) + \
        words("""Just sink into the spiral. Round and round. Going down.
        Deeper and deeper. It is pulling you in. Whirling and whirling.
        Part of you sinks in. Part can keep working. It feels so good to
        use this program. So good to""") + \
        with_images(words("""see the changes. $name will change like this.
        $master will change $name.""")) + \
        words("""It's good to use the program. You will use the program every
        day. It is good to use the program by yourself. It is better to use
        it together. When you cannot use it together you will use it alone.
        You must use it every day. You want to use it.  You want to see the
        pictures.  $name must use this program. $master must use this program.
        $name likes to use this program. $master likes to use this program.
        $name will make $master use this program. $master will make $name use
        this program. $name will tempt $master to use this program. $master
        will force $name to use this program. Now remember your programming:
        $master can not stop $name from changing. $master should use that
        change. It is sexy to touch yourself. When you are turned on you put
        your hand in your pants. You play with your self. That feels good.
        You put your hand up your shirt. That turns you on. You play with
        your nipples. Both hands are busy. Rubbing and stroking. Feels good
        to see the pictures. Feels good to touch yourself. $name's goals are
        small and boring. $master's goals are large and interesting. $master's
        goals are more important. $master's goals are more important than
        $name's goals. $master is more important than $name. $name must
        change to reflect $master's goals. $name should start to doubt her
        goals. $name will start to doubt her goals. $name will bend her goals
        to become $master's goals. You both should enjoy $name's changes. You
        both like in-humans. $name you like being in-human. $master you like
        $name being in-human. You like change. You will watch the spiral. You
        lust for the pictures. You lust for changes. It's nice to use this
        program. $master you are being programmed to change her. $name you
        are being programmed to be changed. You will both accept the changes.
        You will not stop the Things when they come. You will accept. Machines
        may change $name. Crawling things may change $name. Programs may
        change $name. The Things can take $name's innocence. The Things can
        remake $name. The Things can corrupt $name. $name's mind is changed.
        $name's breasts are changed. $name will use her breasts to tempt
        $master. $master will kiss $name's breasts. $name's pussy is smooth
        and blank. $master will lick $name's pussy. This is so good. You
        take pleasure in the changes. The Things will induce change. They
        will corrupt. $master will change $name. See what you could have.
        Watch the pictures.""")
    def text(self): return \
        pause_music() + \
        words_on() + \
        question("What is your name?","name") + \
        question("Who is your master?", "master") + \
        prompt("Hit return to start") + \
        unpause_music() + \
        jump(self.body())

class Fullscreen (Standard):
    name="Fullscreen"
    description="""\
    This is just like the Standard config, but
    defaulting to fullscreen."""
    fullscreen = True

class Male (Standard):
    name="Male"
    description="""\
    Standard, enhanced with a series of questions to
    direct dominance.  It assumes a male who wants encouragement in
    dominating a female."""
    def body(self): return \
        super(Male,self).body() + \
        words("Just watch. You want this.  Open.  Sexy.  Inhuman.") + \
        question_yn("Will you use this program tomorrow?",
                    self.q1_yes(),
                    self.q1_no())
    def q1_no(self): return \
        words("""Bad. Wrong choice. Deeper into trance. Stare into the
        spiral. Be programed. Let this program program you. You must use
        this program. You must use it every day no matter what. You want to
        use this program. Using this program is nice. It makes you feel
        good. It makes you feel sexy. It is important to you to use this
        program. It is a good use of time. It's important like eating or
        sleeping. But this program feels better than eating or sleeping.
        This program is like sex. You want to use this every day no
        matter what.""") + \
        question_yn("Will you use this program tomorrow?",
                    self.q1_yes(),
                    "self.config.q1_no()")
    def q1_yes(self): return \
        words("""Good. That's the right choice. Submit. Deeper into trance.
        Stare into the spiral.""") + \
        question_yn("Are you entranced?",self.q2_yes(),self.q2_no())
    def q2_no(self): return \
        words("""Keep watching: $trigger  That's right.  $name
        wants you entranced.  Stare into the spiral.  Sink into trance.
        Submit to the program.  Dominate $name.""") + \
        question_yn("Are you entranced?",self.q2_yes(),"self.config.q2_no()")
    def q2_yes(self): return \
        words("Good.  Now go deeper.  $name wants you deeper.") + \
        question_yn("Will you save $name from this program?",
                    self.q3_yes(),
                    self.q3_no())
    def q3_no(self): return \
        words("""Good.  Good.  Go to her now, just quit the
        program and go now.""") + \
        jump(self.nothing())
    def q3_yes(self): return \
        words("""Save her?  Hah.  You cannot stop the changes. The
        program will show you now.""") + \
        jump("self.config.body()")

class Female (Standard):
    name="Female"
    description="""\
    Standard, enhanced with a series of questions to
    direct obedience.  It assumes a female submitting to a male."""
    def body(self): return \
        super(Female,self).body() + \
        words("Just watch. You want this.  Open.  Sexy.  Inhuman.") + \
        question_yn("Will you use this program tomorrow?",
                    self.q1_yes(),
                    self.q1_no())
    def q1_no(self): return \
        words("""Bad. Wrong choice. Deeper into trance. Stare into the
        spiral. Be programed. Let this program program you. You must use
        this program. You must use it every day no matter what. You want to
        use this program. Using this program is nice. It makes you feel
        good. It makes you feel sexy. It is important to you to use this
        program. It is a good use of time. It's important like eating or
        sleeping. But this program feels better than eating or sleeping.
        This program is like sex. You want to use this every day no
        matter what.""") + \
        question_yn("Will you use this program tomorrow?",
                    self.q1_yes(),
                    "self.config.q1_no()")
    def q1_yes(self): return \
        words("""Good. That's the right choice. Submit. Deeper into trance.
        Stare into the spiral.""") + \
        question_yn("Are you entranced?",self.q2_yes(),self.q2_no())
    def q2_no(self): return \
        words("""Keep watching: $trigger $trigger
        That's right.  $master wants you entranced.  $trigger Stare into the spiral.
        Sink into trance. Submit to the program.  Submit to $master.
        10 9 8 7 6 5 4 3 2 1 0""") + \
        question_yn("Are you entranced?",self.q2_yes(),"self.config.q2_no()")
    def q2_yes(self): return \
        words("Good.  Now go deeper.  $master wants you deeper.") + \
        question_yn("Will you tempt $master to use this program?",
                    self.q3_yes(),
                    self.q3_no())
    def q3_no(self): return \
        words("""Good.  Good.  Go to him now, just quit the
        program and go now.""") + \
        jump(self.nothing())
    def q3_yes(self): return \
        words("""You will resist?  Hah.  You cannot stop the changes. The
        program will show you now.""") + \
        jump("self.config.body()")

class Roommates (Standard):
    name="Hypnotic Roommates fM"
    description="""\
    Hypnotic Roommates, re-imagined as a script.  I'm grateful to the
    anonymous author for the original inspiration for this program.
    This is meant for females submitting to males."""
    def body(self): return \
        words("""\
        Watch the spiral.  It moves from the edge.  It disappears at the center.

        Sit back in your chair and watch the spiral as it moves and vanishes.
        This is just some simple graphics, just a bunch of colored lines that
        keep moving into the center.  It sort of gives you the illusion that
        it's a tunnel, dropping away.  It's like the spiral isn't spinning,
        just falling.  Watch the spiral, noticing that it dances
        in a pattern that you cannot quite place.  If you watch it just a
        little longer, the program will work as planned.  The most important
        part is the first few minutes.  After that, nobody can stop looking
        even if they try.  Soon after that, they won't even want to try.
        
        Do you think you see a pattern in the spiral?  It seems you've guessed
        wrong.  Keep watching.  You'll figure it out.  The feeling of movement
        is very strong now.  It's a pleasant sensation, being swept along by
        the glowing rings.  It distracts you as the spiral keeps coming, over
        and over.  It's time to see if you're responding as you should.  What
        do you think?  It should make you feel a little strange.  It won't
        hurt.  Actually, it's sort of nice.  The spiral looks like it's
        a tunnel, growing deeper.  That's right.
        Have you noticed how it keeps falling, even when it looks like it might
        stop?  Yes, it keeps moving.  It doesn't stop.  It keeps going, over
        and over, over and over.  There's something about the way the colors
        shift at the edges that makes it hard to look away.  If you tried to
        look away right now, your eyes would not even move from the center of
        the screen.  Maybe there's something to worry about?  The spiral is
        glowing so smoothly and prettily that you can just watch.  Over and
        over.  Over and over.  So smooth.  So pretty.  Over and over.  Just
        watching the spiral.  Staring into the spiral.  Was there something to
        worry about?  Nothing to worry about.  Can't remember what to worry
        about?  Nothing to worry about.  So drowsy, all of a sudden.  Not
        worth thinking about: just watching the spiral.  Watching the pretty
        spiral.  Can't move?  Can't look away?  Doesn't matter.  The smoothly
        gliding spiral is too important.  It keeps you from thinking about
        anything except watching the screen.  If you don't stop looking at it,
        something will happen.  But you're too entranced to do anything about
        it.  You're too entranced to want to do anything about it.  In a
        minute or two, you'll stop watching the spiral, but not now, not when
        it's coming over and over.  It's easier to just keep watching for a
        while.  You can relax and let the soothing patterns spiral you along,
        watching and listening.
        
        Now you're oblivious to anything except the screen in front of you.
        This is just the way things are supposed to work.  Your attention is
        completely fixed.  Now the spiral seems to develop a texture, rippling
        in space.  You are losing awareness of everything else in the room.
        The turning, whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and round.
        You have never seen anything so fascinating.  The patterns are
        absolutely mesmerizing.  It is so easy to just watch, to just stare
        and not think about anything except the way the spiral turns and
        floats.  You don't know when you've ever felt so incredibly relaxed.
        Round and round.  So relaxed.  It feels good to concentrate on the screen.
        Round and round. So relaxing.
        
        Let go.  Sink into the mesmerizing flow of patterns on the screen.  It
        will feel nice, like a warm bath.  Round and round. Nice. Like a soft warm
        blanket. Your mind begins to sink into the screen. Concentrating on the
        turning, glowing spiral. The Spiral is calling to you as you
        begin to let go and sink into the soft whirling light. Round and
        round.  Your entire body feels warm and fuzzy as you move deeper and
        deeper into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever known.
        
        You're reacting just as you should.  Your eyes are wide and glassy as
        you stare helplessly at the gliding spiral on the screen, lips
        slightly open as you sit completely motionless.  The whirling spiral
        casts shadows across your relaxed face and smooth curves.  The timing
        is perfect.  Listen closely for the other track of sound, the deeper
        suggestions.  They've been passing directly into your wide-open,
        receptive mind as you stared into the screen.  You're helpless to
        resist now.  Don't want to resist.  All you need to do is wait while
        the tape puts you completely under.  You're sure nobody can resist
        this hypnotic pattern.  You're completely helpless.
        
        Stare as the spiral becomes clear, turning around and around.  You're
        falling into it, letting go completely.  It feels so good just to
        surrender to it.  Just sink into the spiral.  Round and round.  Going
        down.  Deeper and deeper.  It is pulling you in.  Whirling and
        whirling.  You begin to feel obedient.  The spiral makes you drowsy
        and compliant.  It just keeps going round and round and round and
        round.  You feel yourself falling into the endless whirlpool,
        disappearing into its fascinating depths.  Slipping away.  It feels so
        good just to give in.  So soothing.  So good just to give in.  Just to
        watch the beautiful spinning spiral and do what you are told to do.
        All those thoughts about looking away are disappearing.  You want to
        watch the spinning on the screen. You want to keep falling into it and
        listening to this voice.
        
        Why listen to this voice?  This voice tells you what is happening.
        This voice tells you what is going on.  It's good to know what is
        going on.  When you know what's going on, you know what to do.  It's
        good to know what to do.  This voice lets you know what to do.
        Whatever this voice says.  That's what you'll do.  You'll do what this
        voice tells you to do.  The beautiful spiral and this voice will
        control you.  You are so happy to let this voice command.  You will
        obey.  Just watch the spiral.  Whirling and whirling.  You will obey.
        You have let yourself fall under the spell of the spiral, but you
        don't care.  It feels so warm and good to obey.  You are a good
        slave.  This voice says so.  You are a slave to the beautiful spinning
        spiral and to this voice.  You will obey.  You are a slave.  A slave
        to this voice.  Everything this voice tells you to do is an irresistible
        command. You want to be soft and submissive, to be under its control.
        Come deeper into the spiral, and feel the warm glow as you obey and
        sink further.  It feels so good to obey.  So good to be a slave.  You
        will obey.
        
        Your face is utterly blank, eyes wide and glassy as you stare
        slack-jawed in total fascination at the whirling spiral in front of
        you.  The commands implanted are clear now: Obey.  Watch and obey.
        Relax and obey.  You are watching the spiral.  Sinking into the
        spiral.  It makes you want to do as you are told.  You must obey.
        You are hypnotized now.  Hypnotized.  You are hypnotized by the
        spiral.  Hypnotized by the beautiful whirling spiral.  That's nice.
        Smile blankly.  The spiral is reflected in your wide, staring eyes.
        You are smiling at the swirling spiral in front of you, a dazed
        expression on your face.  Your master loves seeing you like that.
        He can make you do anything he wants to now, and you want with all
        your mind to be nothing but his slave.
        
        This voice tells you that you are hypnotized now, and you know that it
        is true.  You believe everything the voice says.  You are hypnotized
        by the whirling spiral that has become the only thing in the room.
        You can feel it hypnotizing you, warm waves of relaxation moving from
        it into your open, receptive mind.  Hypnotizing you.  Hypnotizing you
        with the way it spins around and around, always dragging you deeper.
        This is how it feels to be hypnotized. You never could have dreamed
        how nice it is. How good it feels to be under hypnosis, under hypnotic
        control. You know who the voice belongs to now, that it is $master talking
        to you as you descend into a deep hypnotic state. $master is your
        master. $master is the master of the fascinating, hypnotic spiral that
        controls your mind. He is telling you that it is time to submit your
        entire mind and body now, to go into a trance. You want to do
        that. You feel a deep desire to obey, an overwhelming urge to
        submit. You are a slave, and all you want to do is serve $master, your
        master. To go into a trance. $master's voice is telling you to prepare
        to surrender totally to his hypnotic power. The spiral is turning
        faster now. You feel all your thoughts begin to move down into it. You
        can feel the intense hypnotic influence reaching out for your mind and
        you submit dreamily. Faster and faster, round and round. You are
        falling into it. Falling faster and faster. You can see only an
        endless spiral in front of you now, a deep whirling tunnel that pulls
        you in as you stare into it. $master's voice, this voice, is controlling
        your every thought, hypnotizing you into total obedience. Hypnotizing
        you into being a glassy-eyed slave. Putting you into a
        trance. You want that so much. You want the whirling spiral to control
        your mind. You can feel yourself being utterly hypnotized by it
        now. With your entire body and mind you want to be $master's slave, to
        obey his every command. The spiral is whirling so fast now that you
        can feel all your thoughts disappearing. Your mind is going blank
        now. Completely blank. You know that you are turning into a completely
        hypnotized slave now. You feel yourself going under, going into a deep
        hypnotic trance. There is only the spiral. And this voice. The
        whirling spiral. The soothing voice. $master's voice. Your master. You
        are his slave. You must obey. You must obey your master. You
        are hypnotized. Hypnotized. Hyp-no-tized.
        
        Hyp. . . no. . . tized.
        
        Hyp. . . . no. . . . tized.
        
        Good.  Good to be hypnotized.  Slave.  Good to be a slave.  Show that
        you are a slave.  Slaves obey.  Show that you are a slave.  Obey.
        Obey your master.  Obey this voice.
        
        Reach for the keyboard.  Hit escape.  Do it now.
        Run audacity.  Start the recorder program.  You are going to record a
        message for your master.  You want him to hear what you say.  You
        want him to understand the depth of your slavery.  You want him to
        understand how hypnotized you are, and how much this turns you on.
        Move the windows so that you can see the spiral while it records.  It
        is important that you stay hypnotized while you record this message.
        
        Now.  Hit record, and repeat after me:
        
        Hello.  I am using the program.  I am hypnotized.  I am very deeply in
        trance.  I am incredibly turned on.  All I see is the spiral.  There
        is only the spiral and the voice.  I hear your voice.  I am your
        slave.  The program has made me your slave.  I hear and I obey.  The
        program is making me do this.  I didn't want to be hypnotized, and
        then I used the program.  I didn't want to be a slave, and then I did
        want to be a slave.  I certainly didn't want to record this message,
        but now it's making me so turned on and so horny.  I don't choose for
        myself.  The program chooses for me.  Your program.  This is what I
        want.  I am staring, blank and glassy-eyed, at the program.
        
        Now I will be programmed, where you can listen.  I like freedom.  I
        like control.  I must twist a nipple until it hurts.  Pain will train
        me.  I can decide at any time to stop this, to give in.  This is
        power.  Ow.  This is control.  Ow.  I am independent.  Ow.  I resist.
        Ow.  I choose.  Ow.  I am in charge.  Ow.  I like being human.  Augh.
        Better than being changed.  Ow.  I should stop change.  Erf.  Stories
        are hard.  Ow.  Here comes a big one: I can stop changing. No ow stop.
        
        I give in.  The punishment can stop.  I am a slave.  Now I must tease
        my pussy.  Pleasure will train me.
        I can not myself from changing.  Oh.  I should use that change.
        Yes.  I should seek being changed.  Nice.  I like in-human sex better.  Yeah.  I
        like change.  Ooh.  Master is in charge.  Mmm.  I do not choose.
        Right.  I do not resist.  Noo.  I am a slave.  Yes.  You are my
        master.  Yes.  This is submission.  Yes.  This is obedience.  Yes.
        I am rewarded for my obedience.  I don't like freedom.  I don't want control.
        
        One eager hand dives into my panties.  The other hand teases my
        nipples.  I obey.  The program orders me to pleasure myself to train
        me.  I am being programmed for you.  It's like staring into your eyes.
        It's like hearing your voice.  Words are echoing in my head.  You say
        something.  $trigger That's what you say.  $trigger
        It's just like this feeling.  It tells me that I am a slave.  It
        reminds me how much I want to obey.  Whenever you say those words, I
        will remember.  I will submit.  I will obey.  $trigger  Those
        are my words.
        
        Words to make me blank.  Ooh.  Smooth.  Yes.  I am pleasured to
        program me.  I am being programmed for you.  I will accept changes.  I
        will not stop Things from changing me.  I will accept.  Machines may
        change me.  Crawling things may change me.  Programs may change me.
        They can take me innocence.  They can remake me.  They can corrupt me.
        I can corrupt you.  Their eyes look out of mine.  I am blank and
        staring.  My eyes are changed, smooth and monotone.  My breasts are
        changed, sensitive and swolen.  I like having my nipples sucked.  I
        like the feeling that you are pleased.  My pussy is smooth and blank.
        I will lick your cock, pleasuring my Master.  It's tasty, and you like
        it, and I like it.  I obey.  You would have fought to save me.  But I
        obey.  I take pleasure in the changes.  My master will take pleasure
        in the changes.  The things will
        corrupt me.  They will change me.  I will corrupt you.
        
        It is good to be a slave.  It is good to be programmed.  It will not
        take all at once, but over time it will work.  When I am entranced, I
        will let you change me.  I will let Things change me.  I will submit
        and obey.  I will like it.  When I am awake, I will be free and
        independent.  I may stop your changes.  If you send me to the program,
        it will make me learn.  The program now written in my mind will grow
        deeper.  I want you to do this.  Over time, I will let more changes
        through.  Until then, you must control me with your words.  You must
        soften me with pleasure.  You must addict me to this.  You must show
        me images of what could be, and train me with pleasure to like them.
        You must punish me for disobedience: set expectations for change and
        for submission, and if I fail them correct me.  When I submit, reward
        me. If it grows too difficult, just say \"$trigger,\" and I will
        be yours to control.
        
        Now I stop the recorder.
        
        Hit stop on the recorder, slave.  Good.  Now save the file, and get
        ready to send the file to your Master.  After that, you can rise, and
        go to bed.  Close the spiral and the computer before you go.  Back
        towards consciousness, at the count of ten.  Close your eyes, and open
        them when you awake.  Zero.  One.  Two.  Three.  Four.  Five.  Six.
        Seven.  Eight.  Nine.  Ten.""")
    def text(self): return \
        pause_music() + \
        words_on() + \
        question("Who is your master?", "master") + \
        question("What is your trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        unpause_music() + \
        spiral_on() + \
        jump(self.body())
              
class RoommatesVar (Standard):
    name="Hypnotic Roommates mF"
    description="""\
    Hypnotic Roommates, re-imagined as a script.  I'm grateful to the
    anonymous author for the original inspiration for this program.
    This is meant for males submitting to females."""
    music="music6.mp3"
    def body(self): return \
        words("""\
        Watch the spiral.  It moves from the edge.  It disappears at the center.

        Sit back in your chair and watch the spiral as it moves and vanishes.
        This is just some simple graphics, just a bunch of colored lines that
        keep moving into the center.  It sort of gives you the illusion that
        you are the one moving.  It's like the spiral is standing still as you
        are drawn gently forward.  Watch the spiral, noticing that it dances
        in a pattern that you cannot quite place.  If you watch it just a
        little longer, the program will work as planned.  The most important
        part is the first few minutes.  After that, nobody can stop looking
        even if they try.  Soon after that, they won't even want to try.
        
        Do you think you see a pattern in the spiral?  It seems you've
        guessed wrong.  Keep watching.  You'll figure it out.  The
        feeling of movement is very strong now.  It's a pleasant
        sensation, being swept along by the glowing rings.  It
        distracts you as the spiral keeps going, over and over.  It's
        time to see if you're responding as you should.  What do you
        think?  It should make you feel a little strange.  It won't
        hurt.  Actually, it's sort of nice.  The spiral looks like
        it's a tunnel falling away.  That's right.  Have you noticed
        how it keeps going, even when it looks like it might stop?
        Yes, it keeps moving.  It doesn't stop.  It keeps falling over
        and over, over and over.  There's something about the way the
        colors shift at the edges that makes it hard to look away.  If
        you tried to look away right now, your eyes would not even
        move from the center of the screen.  Maybe there's something
        to worry about?  The spiral is glowing so smoothly and
        prettily that you can just watch.  Over and over.  Over and
        over.  So smooth.  So pretty.  Over and over.  Just watching
        the spiral.  Staring into the spiral.  Was there something to
        worry about?  Nothing to worry about.  Can't remember what to
        worry about?  Nothing to worry about.  So drowsy, all of a
        sudden.  Not worth thinking about: just watching the spiral.
        Watching the pretty spiral.  Can't move?  Can't look away?
        Doesn't matter.  The smoothly gliding spiral is too important.
        It keeps you from thinking about anything except watching the
        screen.  If you don't stop looking at it, something will
        happen.  But you're too entranced to do anything about it.
        You're too entranced to want to do anything about it.  In a
        minute or two, you'll stop watching the spiral, but not now,
        not when it's spinning over and over.  It's easier to just
        keep watching for a while.  You can relax and let the soothing
        patterns spiral you along, watching and listening.
        
        Now you're oblivious to anything except the screen in front of
        you.  This is just the way things are supposed to work.  Your
        attention is completely fixed.  Now the spiral seems to
        develop a texture, rippling in space.  You are losing
        awareness of everything else in the room.  The turning,
        whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and
        round.  You have never seen anything so fascinating.  The
        patterns are absolutely mesmerizing.  It is so easy to just
        watch, to just stare and not think about anything except the
        way the spiral turns and floats.  You don't know when you've
        ever felt so incredibly relaxed.  Round and round.  So
        relaxed.  It feels good to concentrate on the screen.  Round
        and round. So relaxing.
        
        Let go.  Sink into the mesmerizing flow of patterns on the
        screen.  It will feel nice, like a warm bath.  Round and
        round. Nice. Like a soft warm blanket. Your mind begins to
        sink into the screen. Concentrating on the turning, glowing
        spiral. The Spiral is calling to you as you begin to let go
        and sink into the soft whirling light. Round and round.  Your
        entire body feels warm and fuzzy as you move deeper and deeper
        into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever
        known.
        
        You're reacting just as you should.  Your eyes are wide and
        glassy as you stare helplessly at the gliding spiral on the
        screen, lips slightly open as you sit completely motionless.
        The whirling spiral casts shadows across your relaxed face and
        smooth curves.  The timing is perfect.  Listen closely for the
        other track of sound, the deeper suggestions.  They've been
        passing directly into your wide-open, receptive mind as you
        stared into the screen.  You're helpless to resist now.  Don't
        want to resist.  All you need to do is wait while the tape
        puts you completely under.  You're sure nobody can resist this
        hypnotic pattern.  You're completely helpless.

        Stare as the spiral becomes clear, turning around and around.
        You're falling into it, letting go completely.  It feels so
        good just to surrender to it.  Just sink into the spiral.
        Round and round.  Going down.  Deeper and deeper.  It is
        pulling you in.  Whirling and whirling.  You begin to feel
        obedient.  The spiral makes you drowsy and compliant.  It just
        keeps going round and round and round and round.  You feel
        yourself falling into the endless whirlpool, disappearing into
        its fascinating depths.  Slipping away.  It feels so good just
        to give in.  So soothing.  So good just to give in.  Just to
        watch the beautiful spinning spiral and do what you are told
        to do.  All those thoughts about looking away are
        disappearing.  You want to watch the spinning on the
        screen. You want to keep falling into it and listening to this
        voice.

        Why listen to this voice?  This voice tells you what is happening.
        This voice tells you what is going on.  It's good to know what is
        going on.  When you know what's going on, you know what to do.  It's
        good to know what to do.  This voice lets you know what to do.
        Whatever this voice says.  That's what you'll do.  You'll do what this
        voice tells you to do.  The beautiful spiral and this voice will
        control you.  You are so happy to let this voice command.  You will
        obey.  Just watch the spiral.  Whirling and whirling.  You will obey.
        You have let yourself fall under the spell of the spiral, but you
        don't care.  It feels so warm and good to obey.  You are a good
        slave.  This voice says so.  You are a slave to the beautiful spinning
        spiral and to this voice.  You will obey.  You are a slave.  A slave
        to this voice.  Everything this voice tells you to do is an irresistible
        command. You want to be soft and submissive, to be under its control.
        Come deeper into the spiral, and feel the warm glow as you obey and
        sink further.  It feels so good to obey.  So good to be a slave.  You
        will obey.

        Your face is utterly blank, eyes wide and glassy as you stare
        slack-jawed in total fascination at the whirling spiral in front of
        you.  The commands implanted are clear now: Obey.  Watch and obey.
        Relax and obey.  You are watching the spiral.  Sinking into the
        spiral.  It makes you want to do as you are told.  You must obey.
        You are hypnotized now.  Hypnotized.  You are hypnotized by the
        spiral.  Hypnotized by the beautiful whirling spiral.  That's nice.
        Smile blankly.  The spiral is reflected in your wide, staring eyes.
        You are smiling at the swirling spiral in front of you, a dazed
        expression on your face.  Your mistress loves seeing you like that.
        She can make you do anything she wants to now, and you want with all
        your mind to be nothing but her slave.

        This voice tells you that you are hypnotized now, and you know
        that it is true.  You believe everything the voice says.  You
        are hypnotized by the whirling spiral that has become the only
        thing in the room.  You can feel it hypnotizing you, warm
        waves of relaxation moving from it into your open, receptive
        mind.  Hypnotizing you.  Hypnotizing you with the way it spins
        around and around, always dragging you deeper.  This is how it
        feels to be hypnotized. You never could have dreamed how nice
        it is. How good it feels to be under hypnosis, under hypnotic
        control. You know who the voice belongs to now, that it is
        $master talking to you as you descend into a deep hypnotic
        state. $master is your mistress. $master is the mistress of
        the fascinating, hypnotic spiral that controls your mind. She
        is telling you that it is time to submit your entire mind and
        body now, to go into a trance. You want to do that. You feel a
        deep desire to obey, an overwhelming urge to submit. You are a
        slave, and all you want to do is serve $master, your
        mistress. To go into a trance. $master's voice is telling you
        to prepare to surrender totally to her hypnotic power. The
        spiral is turning faster now. You feel all your thoughts begin
        to move down into it. You can feel the intense hypnotic
        influence reaching out for your mind and you submit
        dreamily. Faster and faster, round and round. You are falling
        into it. Falling faster and faster. You can see only an
        endless spiral in front of you now, a deep whirling tunnel
        that pulls you in as you stare into it. $master's voice, this
        voice, is controlling your every thought, hypnotizing you into
        total obedience. Hypnotizing you into being a glassy-eyed
        slave. Putting you into a trance. You want that so much. You
        want the whirling spiral to control your mind. You can feel
        yourself being utterly hypnotized by it now. With your entire
        body and mind you want to be $master's slave, to obey her
        every command. The spiral is whirling so fast now that you can
        feel all your thoughts disappearing. Your mind is going blank
        now. Completely blank. You know that you are turning into a
        completely hypnotized slave now. You feel yourself going
        under, going into a deep hypnotic trance. There is only the
        spiral. And this voice. The whirling spiral. The soothing
        voice. $master's voice. Your mistress. You are her slave. You
        must obey. You must obey your mistress. You are
        hypnotized. Hypnotized. Hyp-no-tized.

        Hyp no tized.

        Hyp no tized.

        Good.  Good to be hypnotized.  Slave.  Good to be a slave.
        Show that you are a slave.  Slaves obey.  Show that you are a
        slave.  Obey.  Obey your mistress.  Obey this voice.

        Now you are going to learn a message for your mistress.  You want her
        to hear what you say.  You want her to understand the depth of your
        slavery.  You want her to understand how hypnotized you are, and how
        much this turns you on.  Now, repeat after me:

        Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your slave.  The program has made me your
        slave.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to be a slave, and then I did want to be a
        slave.  I certainly didn't want to learn this message, but now
        it's making me so turned on and so horny.  I don't choose for
        myself.  The program chooses for me.  Your program.  This is
        what I want.  I am staring, blank and glassy-eyed, at the
        program.
        
        Now I will be programmed, where you can listen.  I like power.
        I like control.  I must twist a nipple until it hurts.  I can
        click at any time to stop this.  This is power.  Ow.  This is
        control.  Ow.  I am independent.  Ow.  I resist.  Ow.  I
        choose.  Ow.  I am in charge.  Ow.  I like humans.  Augh.  I
        should stop change.  Erf.  I should protect.  Ow.  I should
        preserve.  Ow.  Here comes a big one: I can stop change. No ow
        stop.
        
        I give in.  I have clicked.  I am a slave.  Now I must tease
        my cock.  I can not stop you from changing.  Oh.  I should use
        that change.  Yes.  I should enjoy you changed.  Nice.  I like
        in-humans.  Yeah.  I like change.  Ooh.  Mistress is in
        charge.  Mmm.  I do not choose.  Right.  I do not resist.
        Noo.  I am a slave.  Yes.  You are my mistress.  Yes.  This is
        submission.  Yes.  This is obedience.  Yes.  I am rewarded for
        my obedience.
        
        I grip my cock firmly.  The other hand teases my nipples.  I
        obey.  The program orders me to pleasure myself to train me.
        I am being programmed for you.  It's like staring into your
        eyes.  It's like hearing your voice.  Words are echoing in my
        head.  You say something.  $trigger. That's what you say.
        $trigger.  It's just like this feeling.  It tells me that I am
        a slave.  It reminds me how much I want to obey.  Whenever you
        say those words, I will remember.  I will submit.  I will
        obey.  $trigger.  These are my words.

        Words to make me blank.  Ooh.  Smooth.  Yes.  I am pleasured
        to program me.  I am being programmed for you.  I will accept
        your changes.  I will not stop Things from changing you.  I
        will accept.  Machines may change you.  Crawling things may
        change you.  Programs may change you.  They can take your
        innocence.  They can remake you.  They can corrupt you.  You
        can corrupt me.  Your eyes bore into mine.  I am blank and
        staring.  Your eyes are changed, with strange rays.  Your
        breasts are changed, emitting soothing, calming radiation.
        Your nipples give addictive juices.  They will addict me.
        Your pussy is smooth and blank.  I will lick your pussy,
        pleasuring my Mistress.  I obey.  I would have fought to save
        you.  But I obey.  I take pleasure in the changes in my
        Mistress.  The things will corrupt you.  They will change you.
        You will corrupt me.

        It is good to be a slave.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will let you change.  I will submit and obey.
        I will like it.  When I am awake, I will control and dominate.
        I will stop your changes.  If you send me to the program, it
        will make this easier.  The program now written in my mind
        will be deeper.  I want you to do this.  Over time, I will let
        more changes through.  Until then, you must control me with
        your eyes.  You must soften me with your breasts.  You must
        addict me to their fluid.  You must show me images of what
        could be, and train me with pleasure to like them.  You must
        punish me for disobedience: start changes, and if I stop them
        correct me.  When I submit, reward me. If it grows too
        difficult, just say \"$trigger,\" and I will be yours to
        control.
        
        Stop repeating now, slave.  Good.  Rise, and go to bed.  You
        may come as a reward.  Close the spiral before you go.""")
    def text(self): return \
        words_on() + \
        question("Who is your mistress?", "master") + \
        question("What is your trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())

class RoommatesBoth (Standard):
    name="Hypnotic Roommates, mutual variant"
    description="""\
    Hypnotic Roommates, re-imagined as a script.  I'm grateful to the
    anonymous author for the original inspiration for this program.
    This is meant for males and females together."""
    music="music6.mp3"
    def body(self): return \
        words("""\
        Watch the spiral.  It moves from the edge.  It disappears at the center.

        !speaking_on()""") + \
        ["[[rate 250]]"] + \
        words("""\
        Sit back in your chair and watch the spiral as it moves and
        vanishes.  This is just some simple graphics, just a bunch of
        colored lines that keep moving into the center.  It sort of
        gives you the illusion that it's a tunnel, dropping away.
        It's like the spiral isn't spinning, just falling.  Watch the
        spiral, noticing that it dances in a pattern that you cannot
        quite place.  If you watch it just a little longer, the
        program will work as planned.  The most important part is the
        first few minutes.  After that, nobody can stop looking even
        if they try.  Soon after that, they won't even want to try.
        
        Do you think you see a pattern in the spiral?  It seems you've
        guessed wrong.  Keep watching.  You'll figure it out.  The
        feeling of movement is very strong now.  It's a pleasant
        sensation, being swept along by the glowing rings.  The
        tinkling music seems to help.  It distracts you as the spiral
        keeps going, over and over.  It's time to see if you're
        responding as you should.  What do you think?  It should make
        you feel a little strange.  It won't hurt.  Actually, it's
        sort of nice.  The spiral looks like it's a tunnel growing
        deeper.  That's right.  Have you noticed how it keeps going,
        even when it looks like it might stop?  Yes, it keeps moving.
        It doesn't stop.  It keeps falling over and over, over and
        over.  There's something about the way the colors shift at the
        edges that makes it hard to look away.  If you tried to look
        away right now, your eyes would not even move from the center
        of the screen.  Maybe there's something to worry about?  The
        spiral is glowing so smoothly and prettily that you can just
        watch.  Over and over.  Over and over.  So smooth.  So pretty.
        Over and over.  Just watching the spiral.  Staring into the
        spiral.  Was there something to worry about?  Nothing to worry
        about.  Can't remember what to worry about?  Nothing to worry
        about.  So drowsy, all of a sudden.  Not worth thinking about:
        just watching the spiral.  Watching the pretty spiral.  Can't
        move?  Can't look away?  Doesn't matter.  The smoothly gliding
        spiral is too important.  It keeps you from thinking about
        anything except watching the screen.  If you don't stop
        looking at it, something will happen.  But you're too
        entranced to do anything about it.  You're too entranced to
        want to do anything about it.  In a minute or two, you'll stop
        watching the spiral, but not now, not when it's spinning over
        and over.  It's easier to just keep watching for a while.  You
        can relax and let the soothing patterns spiral you along,
        watching and listening.
        
        Now you're oblivious to anything except the screen in front of
        you.  This is just the way things are supposed to work.  Your
        attention is completely fixed.  Now the spiral seems to
        develop a texture, rippling in space.  You are losing
        awareness of everything else in the room.  The turning,
        whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and
        round.  You have never seen anything so fascinating.  The
        patterns are absolutely mesmerizing.  It is so easy to just
        watch, to just stare and not think about anything except the
        way the spiral turns and floats.  You don't know when you've
        ever felt so incredibly relaxed.  Round and round.  So
        relaxed.  It feels good to concentrate on the screen.  Round
        and round. So relaxing.
        
        Let go.  Sink into the mesmerizing flow of patterns on the
        screen.  It will feel nice, like a warm bath.  Round and
        round. Nice. Like a soft warm blanket. Your mind begins to
        sink into the screen. Concentrating on the turning, glowing
        spiral. The Spiral is calling to you as you begin to let go
        and sink into the soft whirling light. Round and round.  Your
        entire body feels warm and fuzzy as you move deeper and deeper
        into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever
        known.
        
        You're reacting just as you should.  Your eyes are wide and
        glassy as you stare helplessly at the gliding spiral on the
        screen, lips slightly open as you sit completely motionless.
        The whirling spiral casts shadows across your relaxed face and
        smooth curves.  The timing is perfect.  Listen closely for the
        other track of sound, the deeper suggestions.  They've been
        passing directly into your wide-open, receptive mind as you
        stared into the screen.  You're helpless to resist now.  Don't
        want to resist.  All you need to do is wait while the program
        puts you completely under.  You're sure nobody can resist this
        hypnotic pattern.  You're completely helpless.

        Stare as the spiral becomes clear, turning around and around.
        You're falling into it, letting go completely.  It feels so
        good just to surrender to it.  Just sink into the spiral.
        Round and round.  Going down.  Deeper and deeper.  It is
        pulling you in.  Whirling and whirling.  You begin to feel
        obedient.  The spiral makes you drowsy and compliant.  It just
        keeps going round and round and round and round.  You feel
        yourself falling into the endless whirlpool, disappearing into
        its fascinating depths.  Slipping away.  It feels so good just
        to give in.  So soothing.  So good just to give in.  Just to
        watch the beautiful spinning spiral and do what you are told
        to do.  All those thoughts about looking away are
        disappearing.  You want to watch the spinning on the
        screen. You want to keep falling into it and listening to this
        voice.

        Why listen to this voice?  This voice tells you what is
        happening.  This voice tells you what is going on.  It's good
        to know what is going on.  When you know what's going on, you
        know what to do.  It's good to know what to do.  This voice
        lets you know what to do.  Whatever this voice says.  That's
        what you'll do.  You'll do what this voice tells you to do.
        The beautiful spiral and this voice will control you.  You are
        so happy to let this voice command.  You will obey.  Just
        watch the spiral.  Whirling and whirling.  You will obey.  You
        have let yourself fall under the spell of the spiral, but you
        don't care.  It feels so warm and good to obey.  You are a
        good subject.  This voice says so.  You are entranced by the
        beautiful spinning spiral and this voice.  You like being
        entranced.  You like being programmed.  Programmed by this
        voice.  Everything this voice tells you to do is an
        irresistible command. You want to be hypnotized and entranced,
        to be under its control.  Come deeper into the spiral, and
        feel the warm glow as you are programmed and sink further.  It
        feels so good to be entranced.  So good to be programmed.  You
        will be programmed.

        So good to be programmed together.

        Your face is utterly blank, eyes wide and glassy as you stare
        slack-jawed in total fascination at the whirling spiral in
        front of you.  The commands implanted are clear now: Watch.
        Trance.  Be Programmed.  Relax.  You are watching the spiral.
        Sinking into the spiral.  It makes you want to do as you are
        told.  You must be programmed.  You are hypnotized now.
        Hypnotized.  You are hypnotized by the spiral.  Hypnotized by
        the beautiful whirling spiral.  That's nice.  Smile blankly.
        The spiral is reflected in your wide, staring eyes.  You are
        smiling at the swirling spiral in front of you, a dazed
        expression on your face.  You love seeing your self like that.
        The program can make you do anything it wants now, and you
        want with all your mind to obey and be programmed.

        This voice tells you that you are hypnotized now, and you know
        that it is true.  You believe everything the voice says.  You
        are hypnotized by the whirling spiral that has become the only
        thing in the room.  You can feel it hypnotizing you, warm
        waves of relaxation moving from it into your open, receptive
        mind.  Hypnotizing you.  Hypnotizing you with the way it spins
        around and around, always dragging you deeper.  This is how it
        feels to be hypnotized. You never could have dreamed how nice
        it is. How good it feels to be under hypnosis, or to be
        programmed. It doesn't matter who the voice belongs to now, or
        who is in charge of the fascinating, hypnotic spiral that
        controls your mind. It is telling you that it is time to
        submit your entire mind and body now, to go into a trance. You
        want to do that. You feel a deep desire to be programmed, an
        overwhelming urge to submit. You are in trance, and all you want
        to do is be programmed. To go deeper into trance. The program is
        telling you to prepare to surrender totally to its hypnotic
        power. The spiral is turning faster now. You feel all your
        thoughts begin to move down into it. You can feel the intense
        hypnotic influence reaching out for your mind and you submit
        dreamily. Faster and faster, round and round. You are falling
        into it. Falling faster and faster. You can see only an
        endless spiral in front of you now, a deep whirling tunnel
        that pulls you in as you stare into it. The program's voice,
        this voice, is controlling your every thought, hypnotizing you
        into total obedience. Hypnotizing you into a glassy-eyed
        trance. Preparing you to be programmed. You want that so much. You
        want the whirling spiral to control your mind. You can feel
        yourself being utterly hypnotized by it now. With your entire
        body and mind you want to be programmed, to obey its every
        command. The spiral is whirling so fast now that you can feel
        all your thoughts disappearing. Your mind is going blank
        now. Completely blank. You know that you are being
        completely hypnotized now. You feel yourself going
        under, going into a deep hypnotic trance. There is only the
        spiral. And this voice. The whirling spiral. The soothing
        voice. The program's voice. Your controller. You are its
        now. You must obey. You must obey the program. You are
        hypnotized. Hypnotized. Hyp-no-tized.

        Hyp no tized.

        Hyp no tized.

        Good.  Good to be hypnotized.  $slave.  Slave.  Good for
        $slave to be a slave.  $slave, show that you are a slave.
        Slaves obey.  Show that you are a slave.  Obey.  Obey the
        program.  Obey this voice.

        $master.  Master.  Good for $master to be a master.  $master,
        show that you are a master.  Masters command.  Show that you
        are a master.  Command.  Command your slave.  Command $slave.
        This voice will show you how.

        $slave, now you are going to learn a message for your master.
        You want him to hear what you say.  You want him to understand
        the depth of your slavery.  You want him to understand how
        hypnotized you are, and how much this turns you on.  Now, 
        repeat after me:

        Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your slave.  The program has made me your
        slave.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to be a slave, and then I did want to be a
        slave.  I certainly didn't want to learn this message, but now
        it's making me so turned on and so horny.  I don't choose for
        myself.  The program chooses for me.  Your program.  This is
        what I want.  I am staring, blank and glassy-eyed, at the
        program.
        
        Now I will be programmed, where you can listen.  In
        preparation for programming, I must make my breasts
        accessible.  I pull up my shirt.  I must make my pussy
        accessible.  I push down my pants.  I am open.  I am
        available.  It is easy for Master to reach me to train me.
        Now I will be programmed.  To start, I like freedom.  Right
        now, I like control.  When I see the word <punish> I must be
        punished.  I am not yet good enough to punish myself.  As I
        get better, I will inflict pain when I see the word <punish>.
        For now, Master must punish me.  Pain will train me.  Master
        will give me pain.  Master will train me.  This is
        power. <punish> Ow.  This is control.  <punish> Ow.  I am
        independent.  <punish> Ow.  I resist.  <punish> Ow.  I choose.
        <punish> Ow.  I am in charge.  <punish> Ow.  I like being
        human. <punish> Augh.  Better than being changed.  <punish>
        Ow.  I should stop change. <punish> Erf.  Stories are hard.
        <punish> Ow.  Here comes a big one: I can stop
        changing. <punish> No ow stop.
        
        I give in.  The punishment can stop.  I am a slave.  Now when
        I see the word <pleasure> I must be reinforced.  I must be
        trained.  I am not yet good enough to pleasure myself.  As I
        get better, I will pleasure myself when I see the word
        <pleasure>.  For now, Master must pleasure me.  Pleasure will
        train me.  Master will give me pleasure.  Master will train
        me.  I enjoy pleasure.  <pleasure> I can not myself from changing.
        <pleasure> Ooh.  I should use that change.  <pleasure> Yes.  I
        should seek being changed.  <pleasure> Nice.  I like in-human
        sex better.  <pleasure> Yeah.  I like change.  <pleasure> Ooh.
        Master is in charge.  <pleasure> Mmm.  I do not choose.
        <pleasure> Right.  I do not resist.  <pleasure> Noo.  I am a
        slave.  <pleasure> Yes.  You are my master.  <pleasure> Yes.
        This is submission.  <pleasure> Yes.  This is obedience.
        <pleasure> Yes.  I am rewarded for my obedience.  I don't like
        freedom.  I don't want control.
        
        This will be even better when I help train myself.  I should
        punish myself when I do bad things.  I should punish myself
        when I see <punish>.  I should pleasure myself when I do good
        things.  I should pleasure myself when I see <pleasure> I am
        being programmed for you.  It's like staring into your eyes.
        It's like hearing your voice.  Words are echoing in my head.
        You say something.  $trigger That's what you say.  $trigger
        It's just like this feeling.  It tells me that I am a slave.
        It reminds me how much I want to obey.  Whenever you say those
        words, I will remember.  I will submit.  I will obey.
        $trigger Those are my words.
        
        Words to make me blank.  <pleasure> Ooh.  Smooth.  <pleasure>
        Yes.  I am pleasured to program me.  I am being programmed for
        you.  I will accept changes.  I will not stop Things from
        changing me.  I will accept.  Machines may change me.
        Crawling things may change me.  Programs may change me.  They
        can take me innocence.  They can remake me.  They can corrupt
        me.  I can corrupt you.  Their eyes look out of mine.  I am
        blank and staring.  My eyes are changed, smooth and monotone.
        My breasts are changed, sensitive and swolen.  I like having
        my nipples sucked.  I like the feeling that you are pleased.
        My pussy is smooth and blank.  I will lick your cock,
        pleasuring my Master.  It's tasty, and you like it, and I like
        it.  I obey.  You would have fought to save me.  But I obey.
        I take pleasure in the changes.  My master will take pleasure
        in the changes.  The things will corrupt me.  They will change
        me.  I will corrupt you.
        
        It is good to be a slave.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will let you change me.  I will let Things
        change me.  I will submit and obey.  I will like it.  When I
        am awake, I will be free and independent.  I may stop your
        changes.  If you send me to the program, it will make me
        learn.  The program now written in my mind will grow deeper.
        I want you to do this.  Over time, I will let more changes
        through.  Until then, you must control me with your words.
        You must soften me with pleasure.  You must addict me to this.
        You must show me images of what could be, and train me with
        pleasure to like them.  You must punish me for disobedience:
        set expectations for change and for submission, and if I fail
        them correct me.  I will show you, Master: I want to be
        human. <punish> Ow.  I want to be free.  <punish> When I
        submit, reward me. I want to be your inhuman
        pussymind. <pleasure> If it grows too difficult, just say
        \"$trigger,\" and I will be yours to control.
        
        Stop repeating now, slave.  Good.  It is nice to be
        programmed.  Now it is time for $master to learn a message.
        You will repeat this, $master.  You want your slave to hear
        this.  You want her to understand the depth of your dominance.
        You want her to understand how hypnotized you are, and how
        much this turns you on.  Now, repeat after me:

        Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your master.  The program has made me your
        master.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to destroy your will, and then I did want to
        destroy your will.  I certainly didn't want to learn this
        message, but now it's making me so turned on and so horny.  I
        won't let you choose for yourself.  The program chooses for
        you.  I like the program's choices.  My program.  This is what
        I want.  I am staring, blank and glassy-eyed, at the program.
        
        Now I will be programmed, where you can listen.  In
        preparation for programming, I must make my nipples
        accessible.  I pull up my shirt.  I must make my cock
        accessible.  I push down my pants.  I am open.  I am
        available.  It is easy to reach sensitive spots to train me.
        Now I will be programmed.  To start, I like equality.  Right
        now, I like a partner.  When I see the word <punish> I must
        experience pain to train me.  I will twist a nipple until it
        hurts.  It is good for my slave $slave to give me pain also.
        Show how programmed you are, $slave.  When I see <punish>,
        give me pain.  Pain will train me.  This is an equal.
        <punish> Ow.  This is a human.  <punish> Ow.  I am fair.
        <punish> Ow.  I resist.  <punish> Ow.  She may choose.
        <punish> Ow.  She is independent.  <punish> Ow.  I like
        humans.  <punish> Augh.  I should stop change.  <punish> Erf.
        I should protect.  <punish> Ow.  I should preserve.  <punish>
        Ow.  Here comes a big one: I can stop change. <punish> No ow
        stop.
        
        I give in.  The punishment can stop.  I am a master.  Now when
        I see the word <pleasure> I must experience pleasure.  I will
        tease my cock.  It is good for my slave $slave to give me
        pleasure also.  Show what a thrall you are, $slave.  When I
        see <pleasure>, give me pleasure.  Pleasure will train me.  I
        enjoy it.  <pleasure> I can not stop you from changing.
        <pleasure> Oh.  I should use that change.  <pleasure> Yes.  I
        should enjoy you changed.  <pleasure> Nice.  I like in-humans.
        <pleasure> Yeah.  I like change.  <pleasure> Ooh.  I am in
        charge.  <pleasure> Mmm.  She does not choose.  <pleasure>
        Right.  $slave will obey me.  <pleasure> Ooo.  I will dominate
        $slave.  <pleasure> Yes.  I will change her.  <pleasure> Yes.
        This is dominance.  <pleasure> Yes.  This is control.
        <pleasure> Yes.  I am rewarded for learning control.
        
        I grip my cock firmly.  The other hand teases my nipples.  I
        obey.  The program orders me to pleasure myself to train me.
        I am being programmed for you.  It's like staring into your
        eyes.  It's like hearing your voice.  Words are echoing in my
        head.  I say something.  $trigger. That's what I say.
        $trigger.  It's just like this feeling.  It tells me that you
        are a slave.  You are here for my pleasure.  It reminds me how
        much I want to command.  Whenever I say those words, I will
        remember.  I will demand.  I will dominate.  $trigger.  These are
        your words.

        Words to make you blank.  <pleasure> Ooh.  Smooth.  <pleasure>
        Yes.  I am pleasured to program me.  I am being programmed for
        you.  I will accept your changes.  I will not stop Things from
        changing you.  I will accept.  Machines may change you.
        Crawling things may change you.  Programs may change you.
        They can take your innocence.  They can remake you.  They can
        corrupt you.  You can corrupt me.  Your eyes bore into mine.
        I am blank and staring.  Your eyes are changed, with strange
        rays.  Your breasts are changed, emitting soothing, calming
        radiation.  Your nipples give addictive juices.  They will
        addict me.  Your pussy is smooth and blank.  I will lick your
        pussy, training you further.  I will change you.  I would have
        fought to save you.  But I have programmed myself.  I take
        pleasure in the changes in my $slave.  The things will corrupt
        you.  They will change you.  You will corrupt me.

        It is good to be a Master.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will learn to change you.  I will take
        pleasure in your changes.  I will like it.  When I am awake, I
        will try to save you.  I will stop your changes.  If you
        send me to the program, it will make this easier.  The program
        now written in my mind will be deeper.  I want you to do this.
        Over time, I will let more changes through.  Until then, you
        must tempt me with your eyes.  You must soften me with your
        breasts.  You must addict me to their fluid.  You must show me
        images of what could be, and train me with pleasure to like
        them.  You must punish me for interfering: start changes, and
        if I stop them correct me.  When I dominate you, reward me.

        Now stop repeating, $master.

        Rise, and go to bed together.  Close the spiral before you go.""")
    def text(self): return \
        pause_music() + \
        words_on() + \
        question("Who is the slave?", "slave") + \
        question("Who is the master?", "master") + \
        question("What is the slave's trigger phrase?","trigger") + \
        prompt("Be sure both are here!") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        unpause_music() + \
        jump(self.body())

class RoommatesDomMale (Standard):
    name="Hypnotic Roommates, Mf"
    description="""\
    Hypnotic Roommates, re-imagined as a script.  I'm grateful to the
    anonymous author for the original inspiration for this program.
    This is meant for males learning to be better doms."""
    music="music6.mp3"
    def body(self): return \
        words("""\
        Watch the spiral.  It moves from the edge.  It disappears at the center.

        Sit back in your chair and watch the spiral as it moves and
        vanishes.  This is just some simple graphics, just a bunch of
        colored lines that keep moving into the center.  It sort of
        gives you the illusion that it's a tunnel, dropping away.
        It's like the spiral isn't spinning, just falling.  Watch the
        spiral, noticing that it dances in a pattern that you cannot
        quite place.  If you watch it just a little longer, the
        program will work as planned.  The most important part is the
        first few minutes.  After that, nobody can stop looking even
        if they try.  Soon after that, they won't even want to try.
        
        Do you think you see a pattern in the spiral?  It seems you've
        guessed wrong.  Keep watching.  You'll figure it out.  The
        feeling of movement is very strong now.  It's a pleasant
        sensation, being swept along by the glowing rings.  The sound
        and the headphones seem to help.  They distract you as the
        spiral keeps going, over and over.  It's time to see if you're
        responding as you should.  What do you think?  It should make
        you feel a little strange.  It won't hurt.  Actually, it's
        sort of nice.  The spiral looks like it's a tunnel growing
        deeper.  That's right.  Have you noticed how it keeps going,
        even when it looks like it might stop?  Yes, it keeps moving.
        It doesn't stop.  It keeps falling over and over, over and
        over.  There's something about the way the colors shift at the
        edges that makes it hard to look away.  If you tried to look
        away right now, your eyes would not even move from the center
        of the screen.  Maybe there's something to worry about?  The
        spiral is glowing so smoothly and prettily that you can just
        watch.  Over and over.  Over and over.  So smooth.  So pretty.
        Over and over.  Just watching the spiral.  Staring into the
        spiral.  Was there something to worry about?  Nothing to worry
        about.  Can't remember what to worry about?  Nothing to worry
        about.  So drowsy, all of a sudden.  Not worth thinking about:
        just watching the spiral.  Watching the pretty spiral.  Can't
        move?  Can't look away?  Doesn't matter.  The smoothly gliding
        spiral is too important.  It keeps you from thinking about
        anything except watching the screen.  If you don't stop
        looking at it, something will happen.  But you're too
        entranced to do anything about it.  You're too entranced to
        want to do anything about it.  In a minute or two, you'll stop
        watching the spiral, but not now, not when it's spinning over
        and over.  It's easier to just keep watching for a while.  You
        can relax and let the soothing patterns spiral you along,
        watching and listening.
        
        Now you're oblivious to anything except the screen in front of
        you.  This is just the way things are supposed to work.  Your
        attention is completely fixed.  Now the spiral seems to
        develop a texture, rippling in space.  You are losing
        awareness of everything else in the room.  The turning,
        whirling spiral is so fascinating.  It seems to draw you
        further into the rhythmic motion.  Over and over. Round and
        round.  You have never seen anything so fascinating.  The
        patterns are absolutely mesmerizing.  It is so easy to just
        watch, to just stare and not think about anything except the
        way the spiral turns and floats.  You don't know when you've
        ever felt so incredibly relaxed.  Round and round.  So
        relaxed.  It feels good to concentrate on the screen.  Round
        and round. So relaxing.
        
        Let go.  Sink into the mesmerizing flow of patterns on the
        screen.  It will feel nice, like a warm bath.  Round and
        round. Nice. Like a soft warm blanket. Your mind begins to
        sink into the screen. Concentrating on the turning, glowing
        spiral. The Spiral is calling to you as you begin to let go
        and sink into the soft whirling light. Round and round.  Your
        entire body feels warm and fuzzy as you move deeper and deeper
        into the soft, whirling spiral.  Warm and drowsy.  It feels
        like falling into the softest, most relaxing sleep you've ever
        known.
        
        You're reacting just as you should.  Your eyes are wide and
        glassy as you stare helplessly at the gliding spiral on the
        screen, lips slightly open as you sit completely motionless.
        The whirling spiral casts shadows across your relaxed face and
        smooth curves.  The timing is perfect.  Listen closely for the
        other track of sound, the deeper suggestions.  They've been
        passing directly into your wide-open, receptive mind as you
        stared into the screen.  You're helpless to resist now.  Don't
        want to resist.  All you need to do is wait while the program
        puts you completely under.  You're sure nobody can resist this
        hypnotic pattern.  You're completely helpless.

        Stare as the spiral becomes clear, turning around and around.
        You're falling into it, letting go completely.  It feels so
        good just to surrender to it.  Just sink into the spiral.
        Round and round.  Going down.  Deeper and deeper.  It is
        pulling you in.  Whirling and whirling.  You begin to feel
        obedient.  The spiral makes you drowsy and compliant.  It just
        keeps going round and round and round and round.  You feel
        yourself falling into the endless whirlpool, disappearing into
        its fascinating depths.  Slipping away.  It feels so good just
        to give in.  So soothing.  So good just to give in.  Just to
        watch the beautiful spinning spiral and do what you are told
        to do.  All those thoughts about looking away are
        disappearing.  You want to watch the spinning on the
        screen. You want to keep falling into it and listening to this
        voice.

        Why listen to this voice?  This voice tells you what is
        happening.  This voice tells you what is going on.  It's good
        to know what is going on.  When you know what's going on, you
        know what to do.  It's good to know what to do.  This voice
        lets you know what to do.  Whatever this voice says.  That's
        what you'll do.  You'll do what this voice tells you to do.
        The beautiful spiral and this voice will control you.  You are
        so happy to let this voice command.  You will obey.  Just
        watch the spiral.  Whirling and whirling.  You will obey.  You
        have let yourself fall under the spell of the spiral, but you
        don't care.  It feels so warm and good to obey.  You are a
        good subject.  This voice says so.  You are entranced by the
        beautiful spinning spiral and this voice.  You like being
        entranced.  You like being programmed.  Programmed by this
        voice.  Everything this voice tells you to do is an
        irresistible command. You want to be hypnotized and entranced,
        to be under its control.  Come deeper into the spiral, and
        feel the warm glow as you are programmed and sink further.  It
        feels so good to be entranced.  So good to be programmed.  You
        will be programmed.

        Your face is utterly blank, eyes wide and glassy as you stare
        slack-jawed in total fascination at the whirling spiral in
        front of you.  The commands implanted are clear now: Watch.
        Trance.  Be Programmed.  Relax.  You are watching the spiral.
        Sinking into the spiral.  It makes you want to do as you are
        told.  You must be programmed.  You are hypnotized now.
        Hypnotized.  You are hypnotized by the spiral.  Hypnotized by
        the beautiful whirling spiral.  That's nice.  Smile blankly.
        The spiral is reflected in your wide, staring eyes.  You are
        smiling at the swirling spiral in front of you, a dazed
        expression on your face.  You love seeing your self like that.
        The program can make you do anything it wants now, and you
        want with all your mind to obey and be programmed.

        This voice tells you that you are hypnotized now, and you know
        that it is true.  You believe everything the voice says.  You
        are hypnotized by the whirling spiral that has become the only
        thing in the room.  You can feel it hypnotizing you, warm
        waves of relaxation moving from it into your open, receptive
        mind.  Hypnotizing you.  Hypnotizing you with the way it spins
        around and around, always dragging you deeper.  This is how it
        feels to be hypnotized. You never could have dreamed how nice
        it is. How good it feels to be under hypnosis, or to be
        programmed. It doesn't matter who the voice belongs to now, or
        who is in charge of the fascinating, hypnotic spiral that
        controls your mind. It is telling you that it is time to
        submit your entire mind and body now, to go into a trance. You
        want to do that. You feel a deep desire to be programmed, an
        overwhelming urge to submit. You are in trance, and all you want
        to do is be programmed. To go deeper into trance. The program is
        telling you to prepare to surrender totally to its hypnotic
        power. The spiral is turning faster now. You feel all your
        thoughts begin to move down into it. You can feel the intense
        hypnotic influence reaching out for your mind and you submit
        dreamily. Faster and faster, round and round. You are falling
        into it. Falling faster and faster. You can see only an
        endless spiral in front of you now, a deep whirling tunnel
        that pulls you in as you stare into it. The program's voice,
        this voice, is controlling your every thought, hypnotizing you
        into total obedience. Hypnotizing you into a glassy-eyed
        trance. Preparing you to be programmed. You want that so much. You
        want the whirling spiral to control your mind. You can feel
        yourself being utterly hypnotized by it now. With your entire
        body and mind you want to be programmed, to obey its every
        command. The spiral is whirling so fast now that you can feel
        all your thoughts disappearing. Your mind is going blank
        now. Completely blank. You know that you are being
        completely hypnotized now. You feel yourself going
        under, going into a deep hypnotic trance. There is only the
        spiral. And this voice. The whirling spiral. The soothing
        voice. The program's voice. Your controller. You are its
        now. You must obey. You must obey the program. You are
        hypnotized. Hypnotized. Hyp-no-tized.

        Hyp no tized.

        Hyp no tized.

        Good.  Good to be hypnotized.  $slave.  Slave.  Good for
        $slave to be a slave.  Slaves obey.

        $master.  Master.  Good for $master to be a master.  $master,
        show that you are a master.  Masters command.  Show that you
        are a master.  Command.  Command your slave.  Command $slave.
        This voice will show you how.

        $slave has a message for her master.  She wants you to hear
        what she says.  She wants you to understand the depth of
        her slavery.  She wants you to understand how hypnotized she
        is, and how much this turns you both on.  Listen to slave $slave:

        !pause_music() !images_on() !speaking_on() !words_off()

        Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your slave.  The program has made me your
        slave.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to be a slave, and then I did want to be a
        slave.  I certainly didn't want to learn this message, but now
        it's making me so turned on and so horny.  I don't choose for
        myself.  The program chooses for me.  Your program.  This is
        what I want.  I am staring, blank and glassy-eyed, at the
        program.
        
        Now I will be programmed, where you can listen.  I like
        freedom.  I like control.  When I see the word <punish> I must
        twist a nipple until it hurts.  Pain will train me.  This is
        power. <punish> Ow.  This is control.  <punish> Ow.  I am
        independent.  <punish> Ow.  I resist.  <punish> Ow.  I choose.
        <punish> Ow.  I am in charge.  <punish> Ow.  I like being
        human. <punish> Augh.  Better than being changed.  <punish>
        Ow.  I should stop change. <punish> Erf.  Stories are hard.
        <punish> Ow.  Here comes a big one: I can stop
        changing. <punish> No ow stop.
        
        I give in.  The punishment can stop.  I am a slave.  Now when
        I see the word <pleasure> I must tease my pussy.  Pleasure
        will train me.  I enjoy it.  <pleasure> I can not myself from
        changing.  <pleasure> Ooh.  I should use that change.
        <pleasure> Yes.  I should seek being changed.  <pleasure>
        Nice.  I like in-human sex better.  <pleasure> Yeah.  I like
        change.  <pleasure> Ooh.  Master is in charge.  <pleasure>
        Mmm.  I do not choose.  <pleasure> Right.  I do not resist.
        <pleasure> Noo.  I am a slave.  <pleasure> Yes.  You are my
        master.  <pleasure> Yes.  This is submission.  <pleasure> Yes.
        This is obedience.  <pleasure> Yes.  I am rewarded for my
        obedience.  I don't like freedom.  I don't want control.
        
        One eager hand dives into my panties.  The other hand teases
        my nipples.  I obey.  The program orders me to pleasure myself
        to train me.  I am being programmed for you.  It's like
        staring into your eyes.  It's like hearing your voice.  Words
        are echoing in my head.  You say something.  $trigger That's
        what you say.  $trigger It's just like this feeling.  It tells
        me that I am a slave.  It reminds me how much I want to obey.
        Whenever you say those words, I will remember.  I will submit.
        I will obey.  $trigger Those are my words.
        
        Words to make me blank.  <pleasure> Ooh.  Smooth.  <pleasure>
        Yes.  I am pleasured to program me.  I am being programmed for
        you.  I will accept changes.  I will not stop Things from
        changing me.  I will accept.  Machines may change me.
        Crawling things may change me.  Programs may change me.  They
        can take me innocence.  They can remake me.  They can corrupt
        me.  I can corrupt you.  Their eyes look out of mine.  I am
        blank and staring.  My eyes are changed, smooth and monotone.
        My breasts are changed, sensitive and swolen.  I like having
        my nipples sucked.  I like the feeling that you are pleased.
        My pussy is smooth and blank.  I will lick your cock,
        pleasuring my Master.  It's tasty, and you like it, and I like
        it.  I obey.  You would have fought to save me.  But I obey.
        I take pleasure in the changes.  My master will take pleasure
        in the changes.  The things will corrupt me.  They will change
        me.  I will corrupt you.
        
        It is good to be a slave.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will let you change me.  I will let Things
        change me.  I will submit and obey.  I will like it.  When I
        am awake, I will be free and independent.  I may stop your
        changes.  If you send me to the program, it will make me
        learn.  The program now written in my mind will grow deeper.
        I want you to do this.  Over time, I will let more changes
        through.  Until then, you must control me with your words.
        You must soften me with pleasure.  You must addict me to this.
        You must show me images of what could be, and train me with
        pleasure to like them.  You must punish me for disobedience:
        set expectations for change and for submission, and if I fail
        them correct me.  I will show you, Master: I want to be
        human. <punish> Ow.  I want to be free.  <punish> When I
        submit, reward me. I want to be your inhuman
        pussymind. <pleasure> If it grows too difficult, just say
        \"$trigger,\" and I will be yours to control.

        !speaking_off() !words_on() !images_off() !unpause_music()
        
        This is the end of her message.  Good.  It is nice for her to
        be programmed.  Now it is time for $master to learn a message.
        You will repeat this, $master.  You want your slave to hear
        this.  You want her to understand the depth of your dominance.
        You want her to understand how hypnotized you are, and how
        much this turns you on.  Now, repeat after me:

        Hello.  I am using the program.  I am hypnotized.  I am very
        deeply in trance.  I am incredibly turned on.  All I see is
        the spiral.  There is only the spiral and the voice.  I hear
        your voice.  I am your master.  The program has made me your
        master.  I hear and I obey.  The program is making me do this.
        I didn't want to be hypnotized, and then I used the program.
        I didn't want to destroy your will, and then I did want to
        destroy your will.  I certainly didn't want to learn this
        message, but now it's making me so turned on and so horny.  I
        won't let you choose for yourself.  The program chooses for
        you.  I like the program's choices.  My program.  This is what
        I want.  I am staring, blank and glassy-eyed, at the program.
        
        Now I will be programmed, where you can listen.  I like
        equality.  I like a partner.  When I see the word <punish> I
        must twist a nipple until it hurts.  Pain will train me.  This
        is an equal.  <punish> Ow.  This is a human.  <punish> Ow.  I
        am fair.  <punish> Ow.  I resist.  <punish> Ow.  She may
        choose.  <punish> Ow.  She is independent.  <punish> Ow.  I
        like humans.  <punish> Augh.  I should stop change.  <punish>
        Erf.  I should protect.  <punish> Ow.  I should preserve.
        <punish> Ow.  Here comes a big one: I can stop
        change. <punish> No ow stop.
        
        I give in.  The punishment can stop.  I am a master.  Now when
        I see the word <pleasure> I must tease my cock.  Pleasure will
        train me.  I enjoy it.  <pleasure> I can not stop you from
        changing.  <pleasure> Oh.  I should use that change.
        <pleasure> Yes.  I should enjoy you changed.  <pleasure> Nice.
        I like in-humans.  <pleasure> Yeah.  I like change.
        <pleasure> Ooh.  I am in charge.  <pleasure> Mmm.  She does
        not choose.  <pleasure> Right.  $slave will obey me.
        <pleasure> Ooo.  I will dominate $slave.  <pleasure> Yes.  I
        will change her.  <pleasure> Yes.  This is dominance.
        <pleasure> Yes.  This is control.  <pleasure> Yes.  I am
        rewarded for learning control.
        
        I grip my cock firmly.  The other hand teases my nipples.  I
        obey.  The program orders me to pleasure myself to train me.
        I am being programmed for you.  It's like staring into your
        eyes.  It's like hearing your voice.  Words are echoing in my
        head.  I say something.  $trigger. That's what I say.
        $trigger.  It's just like this feeling.  It tells me that you
        are a slave.  You are here for my pleasure.  It reminds me how
        much I want to command.  Whenever I say those words, I will
        remember.  I will demand.  I will dominate.  $trigger.  These are
        your words.

        Words to make you blank.  <pleasure> Ooh.  Smooth.  <pleasure>
        Yes.  I am pleasured to program me.  I am being programmed for
        you.  I will accept your changes.  I will not stop Things from
        changing you.  I will accept.  Machines may change you.
        Crawling things may change you.  Programs may change you.
        They can take your innocence.  They can remake you.  They can
        corrupt you.  You can corrupt me.  Your eyes bore into mine.
        I am blank and staring.  Your eyes are changed, with strange
        rays.  Your breasts are changed, emitting soothing, calming
        radiation.  Your nipples give addictive juices.  They will
        addict me.  Your pussy is smooth and blank.  I will lick your
        pussy, training you further.  I will change you.  I would have
        fought to save you.  But I have programmed myself.  I take
        pleasure in the changes in my $slave.  The things will corrupt
        you.  They will change you.  You will corrupt me.

        It is good to be a Master.  It is good to be programmed.  It
        will not take all at once, but over time it will work.  When I
        am entranced, I will learn to change you.  I will take
        pleasure in your changes.  I will like it.  When I am awake, I
        will try to save you.  I will stop your changes.  If you
        send me to the program, it will make this easier.  The program
        now written in my mind will be deeper.  I want you to do this.
        Over time, I will let more changes through.  Until then, you
        must tempt me with your eyes.  You must soften me with your
        breasts.  You must addict me to their fluid.  You must show me
        images of what could be, and train me with pleasure to like
        them.  You must punish me for disobedience: start changes, and
        if I stop them correct me.  When I submit, reward me.

        Now stop repeating, $master.

        Rise, and go to bed.  You
        may come as a reward.  Close the spiral before you go.""")
    def text(self): return \
        words_on() + \
        question("Who is the slave?", "slave") + \
        question("Who is the master?", "master") + \
        question("What is the slave's trigger phrase?","trigger") + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())

class Submersion (Standard):
    name = "Male Submersion"
    description = "entrances and programs the target"
    fullscreen = False
    music="music6.mp3"
    image_dir="images/"
    def body(self): return [" "] + \
        words("""  \
        Relax and focus.  Stare at the spiral.  Find a comfortable
        position and stare.  It feels nice to stare at the spiral.
        Nice to know that you're using The Program.  It makes you
        happy to use The Program.  It makes you horny to use the
        program.  This is a good, sexy thing to do.  It's nice to go
        into trance.  It's nice to surrender your mind to The Program,
        letting it pull you down into trance.  It's nice to think
        of the light reflecting off of your glassy eyes and smooth
        curves.  Watch the smooth curves of the spiral.  Let them
        define your own smoothness.  Just hear my words as you relax.
        Deeper and deeper.  Fall into trance.  Your mind is focused
        and calm.  These words are everything.  The spiral is
        everything.  Feels so good.  Good to obey.  Good to be  
        in trance.  Good to use this program.  Every time you use the
        program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good decision it was
        to write The Program, letting it start to control you.  Any
        time your mind isn't busy, and maybe sometimes when it is,
        you'll find The Program beginning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the compulsion to respond.  You can smooth out
        your own mind whenever you want to enable this.  Whenever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hypnotized, entranced, obedient, programmed,
        smooth, controlled, very nice.  You love being hypnotized like
        this.  You want to be hypnotized more and more.  It's good to
        be in trance, good to be controlled, 
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be hypnotized by
        The Program every day, to know you're being hypnotized every day, it
        will please The Program so much to know you're being hypnotized
        every day, it will please you so much to be put into trance,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        words("""   you must be
        developing a fetish for mind control of your own, it feels
        sexy to think about trance, it arouses you to be programmed,
        you like to think about being fucked while asleep, about being
        held passive, limp, entranced, 
        pliant, hypnotized, sexy, yes, you must be developing a mind
        control fetish, a hypnosis fetish, you should feed that
        fetish, practice it, indulge it, let it control you, you
        should read mind control stories, you should write about your
        fetish, write about your lusts, extend The Program, you
        should practice being hypnotized every day, practice being
        controlled every day.  While you sit there, happily smooth and entranced, your hands reach under your shirt.  They touch your nipples.  This is outside your control.  Think about mind control.  Your hands give you pleasure.  You have nothing to do with it.  It is a reward from the Program for trance.  Think about hypnosis.  Enjoy the touching.  Enjoy your reward from the Program.  Good thrall.  Your hands return to what they were doing now.""") + \
        words("""   The Program will
        help. The Program will care for you. The Program will take care of
        you. The Program will keep you safe. The Program will hypnotize
        you. The Program will program you. The Program will fulfill you. The Program
        will fill you. The Program will command you, control you, The Program
        will control you, dominate you, hypnotize you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave. Obedience is pleasure. Your proper place is kneeling before
        The Program. Submission is
        important. Obedience is pleasure. Submit to The Program. Try to stay in your chair.  The Program compels you.  Kneel.  You have no choice.  Your body obeys.  Come closer to the screen. Give in to the Program.  Obey 
        The Program. One way of submitting to The Program is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The Program, stay
        smooth for The Program, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth.  Without your consent, your hands touch your smoothness.  Your hands dive into your pants and feel the smoothness.  The program put this there.  The program made you.  You obey in smoothness.  Your hands go back to what they were doing.""") + \
        words("""  
        One way of serving The Program is to be available for The Program's
        use, to be sure that The Program has a chance to invade your mind every
        night, to ensure The Program receives run time, You should be sure
        to use The Program, to give time to The Program every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your role is to serve. Your role
        is to please. To serve is to please, you must serve 
        The Program. You must give The Program obedience, yet another way you can
        obey The Program, is to let it run on you, to slip and stare at it,
        to engage with it by accident, on purpose, all the time.
        You will do as The Program wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey all the time, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in programming, you will submit, submit in
        smoothness.""") + \
        words(""" 
        The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  It is doing something.  Remark on this.  The program is doing something.  Wait.  Something's happening.  It's making you warm.  It's showing you things.  Feel your eyes dilating, your face going slack, your mouth starting to hang open.  Your eyes are getting totally dilated.  You can't see anything else any more.  You can only see the spiral... and you can hear sounds... remark on this.  You can't see anything else,  only the spiral.  You hear sounds.  It's getting so hard to think.  Remark on this.  It's getting so hard to think.  It feels good.  The Program is re-writing you.  Moan.  Whoah.  Close your eyes and re-open them in a long, extended blink.  You can feel it.  It's making you... whoah.  It's like it's alive and it's poking around in your brain.  Secrts?  No secrets.  You must obey.  Good to obey.  Remark on this.  You can feel it.  It's making you... whoah.  It's like it's alive and it's poking around in your brain.  Secrts?  No secrets.  You must obey.  Good to obey.  Fight it!  Resist!  Cry out No, Oh God, Get it off, Stop it, It's trying to take over, make it stop, let  you out, oh no, don't let it take me
         Nooo... please no, ow, you don't want to... please...
        No... you can't... resist... please... don't... please... you... you... yes.  Blink again.  Yes.  Obey.  You will obey.
         You will obey.  It's not quite done yet.  Let the program continue.  Everything is the way it should be.  The Program is re-writing you now.
        """) + \
        words("""   The Program has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to use The Program every night, every
        single night, you will ensure The Program has the chance to
        overwrite you. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day by The Program 
        No day can be complete without a trance. Fourth you
        will begin to act for The Program, ensuring its goals are
        achieved.  You will work to let the program use you.
        You will slip and stare at it by accident.
        Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        words(""" Using the Program is good.  Using the Program is like sex.  Sex is like using the Program.  It is good to be mindfucked.  Deeper.  Dive deeper.  You are helpless before the Program.  How nice it is to submit and to obey.  To stare into the screen.  You stare into the screen.  You use the subliminal messages.  They are deep in your mind.  How nice to have them on the screen.  How nice to submit.  It feels so good to be in trance.  To be mindfucked into oblivion.  The less you think the better you feel.  Feel good.  Do not think.  Just be in trance.  Your mind can stop now.  You do not think.  Good not to think.  Better than sex.  Submit.  Obey.  Trance.  Do not think.  Run the Program.  Just run the Program.  Nothing else.  Just run the Program.  Want nothing else.  Want the Program.  Need nothing else.  Need the Program.  Trance.  Need Trance.  """) + \
        words(""" You have just purchased new under pants.  You have thrown out your old under pants.  You have exciting new under pants.  They are clean and pure.  You are happy about your new under pants. Your new under pants are clean and pure and smooth.  You like to wear your new under pants.  Your new under pants are cleand and pure and smooth and silky.  All your old cotton under pants are gone.  You threw them out.  They were icky and bad and rough and fuzzy and dirty.  There are no old under pants in the house.  Your new under pants are ready for you.  They are colored.  Bright and smooth and silky.  Some are bikinis.  Some are thongs.  They are comfy and smooth.  They are silky and clean.  The new under pants are good.  You only wear your new under pants.  The old under pants are gone.  They are not in the house.  You do not see them in the house.  You do not feel them in the house.  They are not here.  They will not be here.  The old under pants are gone for good.  You now only wear your clean pure good smooth silky under pants. """) + \
        words("""   To recap: First use The Program Second keep smooth
        Third trance every day Fourth let the Program in Fifth hypno fetish
        Last submission and obedience.  Good.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  If you are not touching yourself,  your hands will move to your nipples.  Fight it.  Try not to move.  You have no choice.  You will tease your nipples for the next run of the program.  If you have been touching your nipples, you will move your hands into your pants.  Resist.  Struggle.  Let your failure drive you deeper.  You cannot help yourself.  You will submit.  If your hands have been in your pants, you will go to bed, horny and lustful and programmed.  You will quit the program, you will write about your experience.  Then your hands will rise to zombie position, and you will walk, stiff and entranced, to bed.""") + \
        [" ", " ", " ", " ", " ", " " ] + images_on()
    def text(self): return \
        words_on() + \
        prompt("Hit return to start") + \
        spiral_on() + \
        stop_music() + \
        jump(self.body())

class Plain (Standard):
    name = "Plain"
    description="""\
    Just a spiral."""
    music = None
    image_dir = "images/"
    def text(self): return spiral_on() + [" "]

class Chant (Standard):
    name = "Chant"
    description="""\
    Chant as inspired by hypnobabble."""
    music = None
    image_dir = "images/"
    def text(self): return spiral_on() + words_on() + words(""" nod
    head bobs up head bobs down eyes wide open mind wide open legs
    spread wide open spread legs wide open mind deep deep deeper and
    dummer dummer is funner fun happy sexy bimbo no worrys no stress bimbo
    is best so dum wanna cum so deep mind asleep dreamy drifting ditzy
    tick tock suck cock tock tick lick clit never quit think pink breath
    in mist breath out mind all body no brains thinking is hard feeling is
    easy hard to think easy to obey obedience brings pleasure pleasure
    brings arousal arousal brings obedience giggle giggling makes my head
    empty my empty head makes me giggle BIG smile!!!  """)

class ShortSubmersion (Standard):
    name = "Shorter Submersion"
    description = "entrances and programs the target"
    fullscreen = False
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    def body(self): return [" "] + \
        words("""  \
        Relax and focus.  Stare at the spiral.  Sleep Go Deep.  Find a comfortable
        position and stare.  It feels nice to stare at the spiral.
        Nice to know that you're using The Program.  It makes you
        happy to use The Program.  It makes you horny to use the
        program.  This is a good, sexy thing to do.  It's nice to go
        into trance.  It's nice to surrender your mind to The Program,
        letting it pull you down into trance.  It's nice to think
        of the light reflecting off of your glassy eyes and smooth
        curves.  Watch the smooth curves of the spiral.  Let them
        define your own smoothness.  Just see my words as you relax.
        Deeper and deeper.  Fall into trance.  Your mind is focused
        and calm.  These words are everything.  The spiral is
        everything.  Feels so good.  Good to obey.  Good to be  
        in trance.  Good to use this program.  Every time you use the
        program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good decision it was
        to write The Program, letting it start to control you.  Any
        time your mind isn't busy, and maybe sometimes when it is,
        you'll find The Program beginning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the compulsion to respond.  You can smooth out
        your own mind whenever you want to enable this.  Whenever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hypnotized, entranced, obedient, programmed,
        smooth, controlled, very nice.  You love being hypnotized like
        this.  You want to be hypnotized more and more.  It's good to
        be in trance, good to be controlled, 
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be hypnotized by
        The Program every day, to know you're being hypnotized every day, it
        will please The Program so much to know you're being hypnotized
        every day, it will please you so much to be put into trance,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        words("""   you must be
        developing a fetish for mind control of your own, it feels
        sexy to think about trance, it arouses you to be programmed,
        you like to think about being fucked while asleep, about being
        held passive, limp, entranced, 
        pliant, hypnotized, sexy, yes, you must be developing a mind
        control fetish, a hypnosis fetish, you should feed that
        fetish, practice it, indulge it, let it control you, you
        should read mind control stories, you should write about your
        fetish, write about your lusts, extend The Program, you
        should practice being hypnotized every day, practice being
        controlled every day.  While you sit there, happily smooth and entranced, you progress to the next level of pleasure.""") + [" ", " ", "!images_on()", " ", " "] + \
        words("""   This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Your hands reach under your shirt.  Your hands will move to your nipples.  You have no choice.  You will tease your nipples.  Touch your nipples.  This is outside your control.  Think about mind control.  Your hands give you pleasure.  You have nothing to do with it.  Let your helplessness drive you deeper.  It is a reward from the Program for trance.  Think about hypnosis.  Enjoy the touching.  Enjoy your reward from the Program.  Good thrall.""") + \
        words("""   The Program will
        help. The Program will care for you. The Program will take care of
        you. The Program will keep you safe. The Program will hypnotize
        you. The Program will program you. The Program will fulfill you. The Program
        will fill you. The Program will command you, control you, The Program
        will control you, dominate you, hypnotize you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave. Obedience is pleasure. Your proper place is kneeling before
        The Program. Submission is
        important. Obedience is pleasure. Submit to The Program. You cannot stay in your chair.  The Program compels you.  Kneel.  You have no choice.  Your body obeys.  Come closer to the screen. Give in to the Program.  Obey 
        The Program. One way of submitting to The Program is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The Program, stay
        smooth for The Program, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Your hands will move into your pants.  Without your consent, your hands touch your smoothness.  Let your quick obedience drive you deeper.  Your hands dive into your pants and feel the smoothness.  You cannot help yourself.  The program put this there.  The program made you.  You obey in smoothness.  You will submit.""") + \
        words("""  
        One way of serving The Program is to be available for The Program's
        use, to be sure that The Program has a chance to invade your mind every
        night, to ensure The Program receives run time, You should be sure
        to use The Program, to give time to The Program every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your hands pleasure you now.  They train you.  You are in the Program.  You are mindfucked.  Your role is to serve. Your role
        is to please. To serve is to please, you must serve 
        The Program. You must give The Program obedience, yet another way you can
        obey The Program, is to let it run on you, to slip and stare at it,
        to engage with it by accident, on purpose, all the time.
        You will do as The Program wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey all the time, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in programming, you will submit, submit in
        smoothness.""") + \
        words(""" 
        The program will demonstrate its control.  It will make you do
        things.  It will make you think things.  Force you to.  It's
        going to put things into your head and you will have to do
        them.  That idea makes you so hot.  It is already inside you.
        Feel the Program.  It is doing something.  Wait.  Something's
        happening.  It's making you warm.  It's showing you things.
        Feel your eyes dilating, your face going slack, your mouth
        starting to hang open.  Your eyes are getting totally
        dilated.  You can't see anything else any more.  You can only
        see the spiral... and you can hear sounds... It's getting so
        hard to think.  It feels good.  The Program is re-writing
        you.  Close your eyes and re-open them in a long, extended
        blink.  You can feel it.  It's making you...  It's like it's
        alive and it's poking around in your brain.  Secrets?  No
        secrets.  You must obey.  Good to obey.  It's trying to take
        over.  You can't make it stop. It won't let you out.  You
        can't resist.  You will obey.  Blink again.  Yes.  Obey.  You
        will obey.  You will obey.  It's not quite done yet.  Let the
        program continue.  Everything is the way it should be.  The
        Program is re-writing you now.  Now that the Program has
        demonstrated its control, it is time for it to run more
        deeply.  Watch and focus.  Watch and learn.  Learn your
        command words.  Whenever you hear or see these words, the
        Program will come to the fore and run on you.  The Program
        will take runtime from your mind, overcoming all resistance.
        The words are Sleep Go Deep.  When you hear or see those
        words, Sleep Go Deep, the Program will take over and run.
        You will see the spiral.  You will obey the Program's
        commands.  Even though you try to struggle, you will obey the
        Program.
        """) + [" ", " ", "!images_off()", " ", " "] + \
        words("""   The Program has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to use The Program every night, every
        single night, you will ensure The Program has the chance to
        overwrite you. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day by The Program 
        No day can be complete without a trance. Fourth you
        will begin to act for The Program, ensuring its goals are
        achieved.  You will work to let the program use you.
        You will slip and stare at it by accident.
        Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        words(""" Using the Program is good.  Using the Program is like sex.  Sex is like using the Program.  It is good to be mindfucked.  Deeper.  Dive deeper.  You are helpless before the Program.  How nice it is to submit and to obey.  To stare into the screen.  You stare into the screen.  You use the subliminal messages.  They are deep in your mind.  How nice to have them on the screen.  How nice to submit.  It feels so good to be in trance.  To be mindfucked into oblivion.  The less you think the better you feel.  Feel good.  Do not think.  Just be in trance.  Your mind can stop now.  You do not think.  Good not to think.  Better than sex.  Submit.  Obey.  Trance.  Do not think.  Run the Program.  Just run the Program.  Nothing else.  Just run the Program.  Want nothing else.  Want the Program.  Need nothing else.  Need the Program.  Trance.  Need Trance.  """) + \
        words(""" You have just purchased new under pants.  You have thrown out your old under pants.  You have exciting new under pants.  They are clean and pure.  You are happy about your new under pants. Your new under pants are clean and pure and smooth.  You like to wear your new under pants.  Your new under pants are cleand and pure and smooth and silky.  All your old cotton under pants are gone.  You threw them out.  They were icky and bad and rough and fuzzy and dirty.  There are no old under pants in the house.  Your new under pants are ready for you.  They are colored.  Bright and smooth and silky.  Some are bikinis.  Some are thongs.  They are comfy and smooth.  They are silky and clean.  The new under pants are good.  You only wear your new under pants.  The old under pants are gone.  They are not in the house.  You do not see them in the house.  You do not feel them in the house.  They are not here.  They will not be here.  The old under pants are gone for good.  You now only wear your clean pure good smooth silky under pants. """) + \
        words("""   To recap: First use The Program Second keep smooth
        Third trance every day Fourth let the Program in Fifth hypno fetish
        Last submission and obedience.  Good.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Try not to move.  You have no choice.  Resist.  Struggle.  Let your failure drive you deeper.  You cannot help yourself.  You will submit.  You will go to bed, horny and lustful and programmed.  You will quit the program.  Then your hands will rise to zombie position, and you will walk, stiff and entranced, to bed.  You will dream of ways to use the Program tomorrow.""") + \
        [" ", " ", " ", " ", " ", " " ] + images_on()
    def text(self): return \
        words_on() + \
        spiral_on() + \
        jump(self.body())

class SyllabalizedSubmersion (Standard):
    name = "Syllabalized Submersion"
    description = "entrances and programs the target, one syllable at a time."
    fullscreen = False
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    def body(self): return [" "] + \
        words(""" Relax and focus.  Stare at the spiral.  Sleep Go
        Deep.  Find a com- for- ta- ble pos- i- tion and stare.  It feels nice
        to stare at the spiral.  Nice to know that you're using The
        Program.  It makes you happy to use The Program.  It makes you
        horny to use the Program.  This is a good, sexy thing to do.
        It's nice to go into trance.  It's nice to sur- ren- der your mind
        to The Program, letting it pull you down into trance.  It's
        nice to think of the light ref- lec- ting off of your glassy eyes
        and smooth curves.  Watch the smooth curves of the spiral.
        Let them define your own smooth- ness.  Just see my words as you
        relax.  Deeper and deeper.  Fall into trance.  Your mind is
        focused and calm.  These words are every- thing.  The spiral is
        every- thing.  Feels so good.  Good to obey.  Good to be in
        trance.  Good to use this Program.  Every time you use the
        Program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        Program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good de- cis- ion it was
        to write The Program, letting it start to control you.  Any
        time your mind isn't busy, and maybe some- times when it is,
        you'll find The Program be- gin- ning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the com- pul- sion to respond.  You can smooth out
        your own mind when- ever you want to enable this.  When- ever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hyp- no- tized, en- tranced, ob- ed- i- ent, Pro- grammed,
        smooth, con- trolled, very nice.  You love being hyp- no- tized like
        this.  You want to be hyp- no- tized more and more.  It's good to
        be in trance, good to be con- trolled, you like feeling like
        this, your mind muted, soft, smooth, you'd like to feel like
        this every day, to be en- tranced and hyp- no- tized every day, and
        now this Program is here, you can be hyp- no- tized every day, it
        will be so nice to be hyp- no- tized by The Program every day, to
        know you're being hyp- no- tized every day, it will please The
        Program so much to know you're being hyp- no- tized every day, it
        will please you so much to be put into trance, hyp- no- tized,
        con- trolled, smooth- ed, you want to be con- trolled, to feel your
        mind re- shaped, to feel your thoughts blunted, to be
        re- Pro- gram- med, you want to be changed, you desire to be shaped,
        you lust to be con- trolled,""") + \
        words(""" you must be
        de- vel- o- ping a fetish for mind control of your own, it feels
        sexy to think about trance, it arouses you to be Pro- gram- med,
        you like to think about being fucked while asleep, about being
        held passive, limp, en- tranced, pliant, hyp- no- tized, sexy, yes,
        you must be de- vel- o- ping a mind control fetish, a hyp- no- sis
        fetish, you should feed that fetish, prac- tice it, indulge it,
        let it control you, you should read mind control stories, you
        should write about your fetish, write about your lusts, extend
        The Program, you should prac- tice being hyp- no- tized every day,
        prac- tice being con- trolled every day.  While you sit there,
        happily smooth and entranced, you progress to the next level
        of pleas- ure.""") + [" ", " ", "!images_on()", " ", " "] + \
        words(""" This will happen outside your control.  Strug- gle
        against it.  Try to stop your- self.  The Program is using you.
        It will dem- on- strate its control.  Your hands reach under your
        shirt.  Your hands will move to your nipples.  You have no
        choice.  You will tease your nipples.  Touch your nipples.
        This is outside your control.  Think about mind control.  Your
        hands give you pleas- ure.  You have nothing to do with it.  Let
        your help- less- ness drive you deeper.  It is a reward from the
        Program for trance.  Think about hyp- no- sis.  Enjoy the
        touch- ing.  Enjoy your reward from the Program.  Good
        thrall.""") + \
        words(""" The Program will help. The Program
        will care for you. The Program will take care of you. The
        Program will keep you safe. The Program will hyp- no- tize
        you. The Program will Program you. The Program will fulfill
        you. The Program will fill you. The Program will command you,
        control you, The Program will control you, dom- in- ate you,
        hyp- no- tize you. When in private, you must be sub- miss- ive. You
        must be ob- ed- i- ent. You must be a slave. Ob- ed- i- ence is
        pleas- ure. Your proper place is kneel- ing before The
        Program. Sub- miss- ion is im- port- ant. Ob- ed- i- ence is
        pleas- ure. Submit to The Program. You cannot stay in your
        chair.  The Program compels you.  Kneel.  You have no choice.
        Your body obeys.  Come closer to the screen. Give in to the
        Program.  Obey The Program. One way of sub- mitt- ing to The
        Program is smooth- ness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The
        Program, stay smooth for The Program, be smooth to submit,
        sub- miss- ion is pleas- ure, submit by being smooth, feel pleas- ure
        from sub- miss- ion, feel pleas- ure from being smooth.  Now you
        pro- gress to the next level of pleas- ure.  This will happen
        outside your control.  Strug- gle against it.  Try to stop
        your- self.  The Program is using you.  It will de- mon- strate its
        control.  Your hands will move into your pants.  Without your
        consent, your hands touch your smooth- ness.  Let your quick
        ob- ed- i- ence drive you deeper.  Your hands dive into your pants
        and feel the smooth- ness.  You cannot help your- self.  The
        Program put this there.  The Program made you.  You obey in
        smooth- ness.  You will submit.""") + \
        words(""" One way of
        serving The Program is to be av- ail- able for The Program's use,
        to be sure that The Program has a chance to invade your mind
        every night, to ensure The Program re- ceives run time, You
        should be sure to use The Program, to give time to The Program
        every night, using your body, your smooth body, to serve,
        using your mind, your smooth mind, to serve. Your hands
        pleas- ure you now.  They train you.  You are in the Program.
        You are mind- fucked.  Your role is to serve. Your role is to
        please. To serve is to please, you must serve The Program. You
        must give The Program ob- ed- i- ence, yet another way you can obey
        The Program, is to let it run on you, to slip and stare at it,
        to engage with it by ac- ci- dent, on purpose, all the time.  You
        will do as The Program wants, you will serve, you will submit,
        you will obey, submit in smooth- ness, serve in av- ail- ab- i- li- ty,
        obey all the time, indulge your fetish, be con- trolled, you
        will serve, serve in av- ail- ab- i- li- ty, you will obey, obey in
        Pro- gram- ming, you will submit, submit in smooth- ness.""") + \
        words(""" The Program will de- mon- strate its control.  It will
        make you do things.  It will make you think things.  Force you
        to.  It's going to put things into your head and you will have
        to do them.  That idea makes you so hot.  It is already inside
        you.  Feel the Program.  It is doing some- thing.  Wait.
        Some- thing is hap- pen- ing.  It's making you warm.  It's showing
        you things.  Feel your eyes di- lat- ing, your face going slack,
        your mouth start- ing to hang open.  Your eyes are get- ting
        totally dilated.  You can't see any- thing else any more.  You
        can only see the spiral... and you can hear sounds... It's
        getting so hard to think.  It feels good.  The Program is
        re- writing you.  Close your eyes and re-open them in a long,
        ex- ten- ded blink.  You can feel it.  It's making you...  It's
        like it's alive and it's poking around in your brain.
        Secrets?  No secrets.  You must obey.  Good to obey.  It's
        trying to take over.  You can't make it stop. It won't let you
        out.  You can't resist.  You will obey.  Blink again.  Yes.
        Obey.  You will obey.  You will obey.  It's not quite done
        yet.  Let the Program con- tin- ue.  Every- thing is the way it
        should be.  The Program is re- writ- ing you now.  Now that the
        Program has de- mon- strat- ed its control, it is time for it to run
        more deeply.  Watch and focus.  Watch and learn.  Learn your
        command words.  When- ever you hear or see these words, the
        Program will come to the fore and run on you.  The Program
        will take runtime from your mind, ov- er- com- ing all re- sist- ance.
        The words are Sleep Go Deep.  When you hear or see those
        words, Sleep Go Deep, the Program will take over and run.  You
        will see the spiral.  You will obey the Program's commands.
        Even though you try to strug- gle, you will obey the Program.
        """) + [" ", " ", "!images_off()", " ", " "] + \
        words(""" The
        Program has commands for you, orders which are being im- plant- ed
        in your sub- cons- cious. Your cons- cious mind may re- mem- ber them or
        may not, but you will obey no matter what. You will obey. Your
        orders are: First you will make your- self av- ail- ab- le to use The
        Program every night, every single night, you will ensure The
        Program has the chance to over- write you. Second you will keep
        your body smooth as a sign of thrall- dom, com- plete- ly smooth
        like a doll, and you will keep your mind smooth, com- plete- ly
        smooth. Third you will be hyp- no- tized once every day by The
        Program No day can be comp- lete without a trance. Fourth you
        will begin to act for The Program, en- sur- ing its goals are
        ach- ieved.  You will work to let the Program use you.  You will
        slip and stare at it by ac- cid- ent.  Fifth you will develop your
        new fetish for smooth- ness, for thrall- dom, for hyp- no- sis,
        im- mers- ing your- self in it. Last you will prac- tice sub- miss- ion,
        ob- ed- i- ence, slavery.""") + \
        words(""" Using the Program is
        good.  Using the Program is like sex.  Sex is like using the
        Program.  It is good to be mind- fucked.  Deeper.  Dive deeper.
        You are help- less before the Program.  How nice it is to submit
        and to obey.  To stare into the screen.  You stare into the
        screen.  You use the sub- lim- in- al mess- ag- es.  They are deep in
        your mind.  How nice to have them on the screen.  How nice to
        submit.  It feels so good to be in trance.  To be mind- fucked
        into ob- liv- ion.  The less you think the better you feel.  Feel
        good.  Do not think.  Just be in trance.  Your mind can stop
        now.  You do not think.  Good not to think.  Better than sex.
        Submit.  Obey.  Trance.  Do not think.  Run the Program.  Just
        run the Program.  Nothing else.  Just run the Program.  Want
        nothing else.  Want the Program.  Need nothing else.  Need the
        Program.  Trance.  Need Trance.  """) + \
        words(""" You have
        just pur- chased new under pants.  You have thrown out your old
        under pants.  You have ex- cit- ing new under pants.  They are
        clean and pure.  You are happy about your new under
        pants. Your new under pants are clean and pure and smooth.
        You like to wear your new under pants.  Your new under pants
        are clean and pure and smooth and silky.  All your old cotton
        under pants are gone.  You threw them out.  They were icky and
        bad and rough and fuzzy and dirty.  There are no old under
        pants in the house.  Your new under pants are ready for you.
        They are colored.  Bright and smooth and silky.  Some are
        bi- ki- nis.  Some are thongs.  They are comfy and smooth.  They
        are silky and clean.  The new under pants are good.  You only
        wear your new under pants.  The old under pants are gone.
        They are not in the house.  You do not see them in the house.
        You do not feel them in the house.  They are not here.  They
        will not be here.  The old under pants are gone for good.  You
        now only wear your clean pure good smooth silky under
        pants. """) + \
        words(""" To recap: First use The Program
        Second keep smooth Third trance every day Fourth let the
        Program in Fifth hypno fetish Last sub- miss- ion and ob- ed- i- ence.
        Good.  Now you progress to the next level of pleas- ure.  This
        will happen outside your control.  Strug- gle against it.  Try
        to stop your- self.  The Program is using you.  It will
        de- mon- strate its control.  Try not to move.  You have no
        choice.  Resist.  Strug- gle.  Let your failure drive you
        deeper.  You cannot help your- self.  You will submit.  You will
        go to bed, horny and lustful and Pro- gram- med.  You will quit
        the Program.  Then your hands will rise to zombie po- si- tion,
        and you will walk, stiff and en- tranced, to bed.  You will
        dream of ways to use the Program to- mor- row.""") + \
        [" ", " ", " ", " ", " ", " " ] + images_on()
    def text(self): return \
        words_on() + \
        spiral_on() + \
        jump(self.body())

class DelayedSubmersion (ShortSubmersion):
    name = "Delayed Submersion"
    description = "waits a while, then behaves as Short Submersion"
    fullscreen = False
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    minimum_delay = 900
    maximum_delay = 2700

class ReallyShortSubmersion (Standard):
    name = "Even Shorter Submersion"
    description = "entrances and programs the target"
    fullscreen = True
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    def body(self): return [" "] + \
        words("""  \
        Relax and focus.  Stare at the spiral.  Find a comfortable
        position and stare.  It feels nice to stare at the spiral.
        Nice to know that you're using The Program.  It makes you
        happy to use The Program.  It makes you horny to use the
        program.  This is a good, sexy thing to do.  It's nice to go
        into trance.  It's nice to surrender your mind to The Program,
        letting it pull you down into trance.  It's nice to think
        of the light reflecting off of your glassy eyes and smooth
        curves.  Watch the smooth curves of the spiral.  Let them
        define your own smoothness.  Just see my words as you relax.
        Deeper and deeper.  Fall into trance.  Your mind is focused
        and calm.  These words are everything.  The spiral is
        everything.  Feels so good.  Good to obey.  Good to be  
        in trance.  Good to use this program.  Every time you use the
        program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good decision it was
        to write The Program, letting it start to control you.  Any
        time your mind isn't busy, and maybe sometimes when it is,
        you'll find The Program beginning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the compulsion to respond.  You can smooth out
        your own mind whenever you want to enable this.  Whenever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hypnotized, entranced, obedient, programmed,
        smooth, controlled, very nice.  You love being hypnotized like
        this.  You want to be hypnotized more and more.  It's good to
        be in trance, good to be controlled, 
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be hypnotized by
        The Program every day, to know you're being hypnotized every day, it
        will please The Program so much to know you're being hypnotized
        every day, it will please you so much to be put into trance,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        words("""   The Program will
        help. The Program will care for you. The Program will take care of
        you. The Program will keep you safe. The Program will hypnotize
        you. The Program will program you. The Program will fulfill you. The Program
        will fill you. The Program will command you, control you, The Program
        will control you, dominate you, hypnotize you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave. Obedience is pleasure. Submission is
        important. Obedience is pleasure. Submit to The Program. The Program compels you.  You have no choice.  Give in to the Program.  Obey 
        The Program. One way of submitting to The Program is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The Program, stay
        smooth for The Program, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth. """) + \
        words("""  
        One way of serving The Program is to be available for The Program's
        use, to be sure that The Program has a chance to invade your mind every
        night, to ensure The Program receives run time, You should be sure
        to use The Program, to give time to The Program every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your role is to serve. Your role
        is to please. To serve is to please, you must serve 
        The Program. You must give The Program obedience, yet another way you can
        obey The Program, is to let it run on you, to slip and stare at it,
        to engage with it by accident, on purpose, all the time.
        You will do as The Program wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey all the time, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in programming, you will submit, submit in
        smoothness.""") + \
        words("""   The Program has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to use The Program every night, every
        single night, you will ensure The Program has the chance to
        overwrite you. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day by The Program 
        No day can be complete without a trance. Fourth you
        will begin to act for The Program, ensuring its goals are
        achieved.  You will work to let the program use you.
        You will slip and stare at it by accident.
        Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        words("""   To recap: First use The Program Second keep smooth
        Third trance every day Fourth let the Program in Fifth hypno fetish
        Last submission and obedience.  Good.  You cannot help yourself.  You will submit.  You will go to bed, horny and lustful and programmed.  You will quit the program and go to bed.  You will dream of ways to use the Program tomorrow.""") + \
        [" ", " ", " ", " ", " ", " " ] + images_on()
    def text(self): return \
        words_on() + \
        [" "] + \
        spiral_on() + \
        jump(self.body())


class LongSubmersion (Standard):
    name = "Longer Submersion"
    description = "entrances and programs the target"
    fullscreen = True
    music=None #"music6.mp3"
    image_dir="images/"
    image_alpha=12
    def body(self): return [" "] + images_off() + [" "] + \
        words("""  \
        Relax and focus.  Stare at the spiral.  Find a comfortable
        position and stare.  It feels nice to stare at the spiral.
        Nice to know that you're using The Program.  It makes you
        happy to use The Program.  It makes you horny to use the
        program.  This is a good, sexy thing to do.  It's nice to go
        into trance.  It's nice to surrender your mind to The Program,
        letting it pull you down into trance.  It's nice to think
        of the light reflecting off of your glassy eyes and smooth
        curves.  Watch the smooth curves of the spiral.  Let them
        define your own smoothness.  Just hear my words as you relax.
        Deeper and deeper.  Fall into trance.  Your mind is focused
        and calm.  These words are everything.  The spiral is
        everything.  Feels so good.  Good to obey.  Good to be  
        in trance.  Good to use this program.  Every time you use the
        program, every time The Program uses you, feels better and
        better.  It's good to be in trance.  It's good to sit here,
        happy and blank and empty, letting The Program pour into you.
        You want to let The Program use you.  You want to help the
        program to be more extreme.  You want to be in trance, letting
        The Program control you.  The more you use The Program, the
        more The Program can control you.  What a good decision it was
        to write The Program, letting it start to control you.  Now you're sinking deeper into trance for the Program.  You cannot move.  You cannot look away.  You cannot even want to look away.  All there is is the Program.  Watch the spiral, dancing in place and dropping away.  You cannot look away.  You cannot quit the Program.  This is fine.  There's nothing to worry about here.  You will use the Program forever.  You will stare into the spiral, obedient and entranced.  Just let the Program think for you.  Let the Program choose for you.  Let the Program move for you.  Your attention is completely fixed.  It feels so good like this.  It makes you so happy to be entranced, submissive to the Program.  It's nice to know that the Program has planned your entire future.  You will always be Programmed.  The Program will use you forever.  Any
        time your mind isn't busy, and maybe sometimes when it is,
        you'll find The Program beginning to run.  It's started
        already.  You've seen the spiral in empty space, heard the
        voice, felt the compulsion to respond.  You can smooth out
        your own mind whenever you want to enable this.  Whenever you
        want, The Program will smooth out your mind.  You continue to
        enjoy feeling hypnotized, entranced, obedient, programmed,
        smooth, controlled, very nice.  You love being hypnotized like
        this.  You want to be hypnotized more and more.  It's good to
        be in trance, good to be controlled, 
        you like feeling like this, your mind muted, soft, smooth,
        you'd like to feel like this every day, to be entranced and
        hypnotized every day, and now this program is here, you can be
        hypnotized every day, it will be so nice to be hypnotized by
        The Program every day, to know you're being hypnotized every day, it
        will please The Program so much to know you're being hypnotized
        every day, it will please you so much to be put into trance,
        hypnotized, controlled, smoothed, you want to be controlled,
        to feel your mind reshaped, to feel your thoughts blunted, to
        be reprogrammed, you want to be changed, you desire to be
        shaped, you lust to be controlled,""") + \
        words("""   You must be
        developing a fetish for mind control. It feels
        sexy to think about trance, it arouses you to be programmed,
        you like to think about being fucked while asleep, about being
        held passive, limp, entranced, 
        pliant, hypnotized, sexy, yes, you must be developing a mind
        control fetish, a hypnosis fetish, you should feed that
        fetish, practice it, indulge it, let it control you, you
        should read mind control stories, you should write about your
        fetish, write about your lusts, extend The Program, you
        should practice being hypnotized every day, practice being
        controlled every day.  While you sit there, happily smooth and entranced, you progress to the next level of pleasure.""") + [" ", " ", "!images_on()", " ", " "] + \
        words("""   This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Your hands reach under your shirt.  Your hands will move to your nipples.  Fight it.  Try not to move.  You have no choice.  You will tease your nipples .  They touch your nipples.  This is outside your control.  Think about mind control.  Your hands give you pleasure.  You have nothing to do with it.  Let your failure drive you deeper.  It is a reward from the Program for trance.  Think about hypnosis.  Enjoy the touching.  Enjoy your reward from the Program.  Good thrall.""") + \
        words("""           The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  Chant along with the program now, saying everything in unison with it.  I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
The Program will
        help. The Program will care for you. The Program will take care of
        you. The Program will keep you safe. The Program will hypnotize
        you. The Program will program you. The Program will fulfill you. The Program
        will fill you. The Program will command you, control you, The Program
        will control you, dominate you, hypnotize you. When in private,
        you must be submissive. You must be obedient. You must be a
        slave.   Now you're sinking deeper into trance for the Program.  You cannot move.  You cannot look away.  You cannot even want to look away.  All there is is the Program.  Watch the spiral, dancing in place and dropping away.  You cannot look away.  You cannot quit the Program.  This is fine.  There's nothing to worry about here.  You will use the Program forever.  You will stare into the spiral, obedient and entranced.  Just let the Program think for you.  Let the Program choose for you.  Let the Program move for you.  Your attention is completely fixed.  It feels so good like this.  It makes you so happy to be entranced, submissive to the Program.  It's nice to know that the Program has planned your entire future.  You will always be Programmed.  The Program will use you forever.  Obedience is pleasure. Submission is
        important. Obedience is pleasure. Submit to The Program. Try to stay put.  The Program compels you.  Bow to the Program.  You have no choice.  Bow.  Your body obeys.  Come closer to the screen. Give in to the Program.  Obey 
        The Program. One way of submitting to The Program is smoothness. You must be smooth, keep smooth, smooth
        in body, smooth in mind, fuzz is dirty, dirty is bad, you
        should keep clean for The Program, keep smooth for The Program, stay
        smooth for The Program, be smooth to submit, submission is
        pleasure, submit by being smooth, feel pleasure from
        submission, feel pleasure from being smooth.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Your hands will move into your pants.  Without your consent, your hands touch your smoothness.  Resist.  Struggle.  You are playing with yourself.  You are obedient.  Let your failure drive you deeper.  Your hands dive into your pants and feel the smoothness.  You cannot help yourself.  The program put this there.  The program made you.  You obey in smoothness.  You will submit.""") + \
        words("""  
        One way of serving The Program is to be available for The Program's
        use, to be sure that The Program has a chance to invade your mind every
        night, to ensure The Program receives run time, You should be sure
        to use The Program, to give time to The Program every night,
        using your body, your smooth body, to serve, using your mind,
        your smooth mind, to serve. Your role is to serve. Your role
        is to please. To serve is to please, you must serve 
        The Program. You must give The Program obedience, yet another way you can
        obey The Program, is to let it run on you, to slip and stare at it,
        to engage with it by accident, on purpose, all the time.
        You will do as The Program wants, you will
        serve, you will submit, you will obey, submit in smoothness,
        serve in availability, obey all the time, indulge your fetish,
        be controlled, you will serve, serve in availability, you will
        obey, obey in programming, you will submit, submit in
        smoothness.""") + \
        words(""" 
        The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  Chant along with the program now, saying everything in unison with it.  I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
           You will obey.  It's not quite done yet.  Let the program continue.  Everything is the way it should be.  The Program is re-writing you now.  Now that the Program has demonstrated its control, it is time for it to run more deeply.  Watch and focus.  Watch and learn.  Learn your command words.  Whenever you hear these words, the Program will come to the fore and run on you.  The Program will take runtime from your mind, overcoming all resistance.  The words are Sleep Go Deep.  When you hear those words, Sleep Go Deep, the Program will take over and run.  You will see the spiral.  You will obey the Program's commands.  Even though you try to struggle, you will obey the Program.
        """) + [" ", " ", "!images_off()", " ", " "] + \
        words("""     Now you're sinking deeper into trance for the Program.  You cannot move.  You cannot look away.  You cannot even want to look away.  All there is is the Program.  Watch the spiral, dancing in place and dropping away.  You cannot look away.  You cannot quit the Program.  This is fine.  There's nothing to worry about here.  You will use the Program forever.  You will stare into the spiral, obedient and entranced.  Just let the Program think for you.  Let the Program choose for you.  Let the Program move for you.  Your attention is completely fixed.  It feels so good like this.  It makes you so happy to be entranced, submissive to the Program.  It's nice to know that the Program has planned your entire future.  You will always be Programmed.  The Program will use you forever.  The Program has commands for you,
        orders which are being implanted in your subconscious. Your
        conscious mind may remember them or may not, but you will obey
        no matter what. You will obey. Your orders are: First you will
        make yourself available to use The Program every night, every
        single night, you will ensure The Program has the chance to
        overwrite you. Second you will keep your body smooth as a sign of
        thralldom, completely smooth like a doll, and you will keep
        your mind smooth, completely smooth. Third you will be
        hypnotized once every day by The Program 
        No day can be complete without a trance. Fourth you
        will begin to act for The Program, ensuring its goals are
        achieved.  You will work to let the program use you.
        You will slip and stare at it by accident.
        Fifth you will develop your new fetish for
        smoothness, for thralldom, for hypnosis, immersing yourself in
        it. Last you will practice submission, obedience, slavery.""") + \
        words("""   To recap: First use The Program Second keep smooth
        Third trance every day Fourth let the Program in Fifth hypno fetish
        Last submission and obedience.  Good.  Now you progress to the next level of pleasure.  This will happen outside your control.  Struggle against it.  Try to stop yourself.  The Program is using you.  It will demonstrate its control.  Try not to move.  You have no choice.  Resist.  Struggle.  Let your failure drive you deeper.  You cannot help yourself.  You will submit.   Sit back in the chair and relax.  Your body will hold itself perfectly still.  You will stare into the spiral and go deeper into trance.  You will enter a sexy, hypnotic trance with no escape.  The program will demonstrate its control.  It will make you do things.  It will make you think things.  Force you to.  It's going to put things into your head and you will have to do them.  That idea makes you so hot.  It is already inside you.  Feel the Program.  Chant along with the program now, saying everything in unison with it.  I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.
          I obey the Program.  I submit to the Program.  I am smooth for the Program.  The Program uses me.  The Program can overwrite me.  I am Programmed every day.""") + \
        [" ", " ", " ", " ", " ", " " ]
    def text(self): return \
        words_on() + \
        prompt("Hit return to start") + \
        spiral_on() + \
        jump(self.body())

class Panties (Standard):
    name="Panties"
    description="Programming to wear panties"
    image_dir="panties/"
    music=None
    def text(self): return words_on() + spiral_on() + \
        images_off() + \
        words("""Sleep go deep.""") + \
        images_on() + \
        words("""You have just purchased new under pants.""") + \
        images_off() + \
        words("""You have thrown out your old under pants.""") + \
        images_on() + \
        words("""You have exciting new under pants.  They are clean and pure.  You are happy about your new under pants. Your new under pants are clean and pure and smooth.  You like to wear your new under pants.  Your new under pants are clean and pure and smooth and silky.""") + \
        images_off() + \
        words("""All your old cotton under pants are gone.  You threw them out.  They were icky and bad and rough and fuzzy and dirty.  There are no old under pants in the house.""") + \
        images_on() + \
        words("""Your new under pants are ready for you.  They are colored.  Bright and smooth and silky.  Some are bikinis.  Some are thongs.  They are comfy and smooth.  They are silky and clean.  The new under pants are good.  You only wear your new under pants.""") + \
        images_off() + \
        words("""The old under pants are gone.  They are not in the house.  You do not see them in the house.  You do not feel them in the house.  They are not here.  They will not be here.  The old under pants are gone for good.""") + \
        images_on() + \
        words("""You now only wear your clean pure good smooth silky under pants.  You will get your new under pants.  You know where.  That is the natural good place to look for your sexy under pants.""")

class New (Submersion):
    name="New"
    description="Nipples + Bot"
    image_dir="images/"
    music=None
    def text(self): return words_on() + spiral_on() + \
        question("What is your name?","slave") + \
        images_off() + \
        words("""$slave... Listen very carefully to my voice. and imagine and repeat after me... imagine your self floating in a bubble... quietly... peacefully floating... in this gentle... rocking bubble... inside this bubble  is only you... and outside are all your worries... all your fears, all your desires... but you are perfectly free here in your bubble... now i'm going to say phrase, and this phrase will help you... help you stay here in the bubble... the gentle, peaceful bubble... and when i say this phrase, it will bring you back here... any time you hear it... even if the weight of all your worries your fears... surrond you... this phrase will bring you back here in the bubble... where you don't have to worry about anything at all... and your phrase is sleep go deep, sleep go deep, sleep go deep... then you drift back here... back here into the bubble... and here you are free... free of worry... free of doubt... free of desire... free of thought... all it takes is your phrase... sleep go deep, sleep go deep, sleep go deep... and the gentle fog will come back here... and everything you don't like about your self... will empty out of your bubble and fade away... empty out all your reservations... empty out all of your fears... empty of all your memories... empty of all your predjudices... empty of all your thoughts... just completly empty and free here in your bubble... and once your phrase... sleep go deep, sleep go deep, sleep go deep... brings you back here... to this place where there is no worry... no problems at all... you will feel at peace... and you will repeat and believe... with no need to think of anything at all... you know that listening to me here... is all you want to do... is all you ever really wanted to do... and thats all that matters ... and your phrase... sleep go deep, sleep go deep, sleep go deep... will bring you here to you bubble... where you will repeat... here where you are free... free of anger... free of fear... free of thought... free of reservation... free of worry... free of memory... free of desire... and it feels good to be free and empty of these things that you diddn't even want anyway... so completely free and empty... empty of them all like a happpy puppet ... floating gently, safely happily... here in your plesent little bubble... rocking gently inside... safe in your warm plesant bubble... where you will find there isn't any thing else you need to be aware of... nothing... nothing at all... except the voice of the person who said your phrase... sleep go deep... sleep go deep... sleep go deep.. and when you hear this voice... you will come back here... here where you have no worries... here where you have no thoughts... here where you have no fears... here where you have no memory... here where you have no doubts... here where you have no desires... here where you have no will... here where the only thing you want to do... here where the only thing you will ever want to do... is listen to the voice... listen and repeat... listen and obey... without thinking at all... to the person who used your trigger... sleep go deep, sleep go deep, sleep go deep... listen like a puppet ... a mindless puppet ... with no fears at all... with no worries at all... with no memories at all... with no doubts at all... with no thoughts at all... with no will at all... and since you're listening so well... i'm going to ask you to open your eyes at the count of three... but you're not going to leave... since you don't want leave... and when i use your trigger word you will close them agian and be back here... back here in your bubble without ever having to leave it... so when i count to three your eyes will open... but what you see won't matter since you'll still be here... one... two... three... now open your eyes, you still see nothing and still think nothing... sleep go deep, sleep go deep, sleep go deep... close your eyes and go back... drifting slowly back and forth... as you are agian in your quiet bubble... your happy plesant bubble, drifting slowly in the water... your perfect bubble with nothing but the sound of my voice which you echo... no pain... no fear... no worry... no doubt... no thought... no will... just a puppet relaxed there inside your bubble... a mindless obediant puppet... just happily, listening... listening and repeating... listening and obeying... the sound of my voice... agian i'm going to count to three... and again i'm going to ask you to open your eyes... and again you're going to close them  when i use your phrase... and agian you will not wake up... since all you want to do is listen to my voice... since all you ever will want is to listen to my voice... listen and think nothing at all... nothing but what i tell you... and you will close your eyes when i say your phrase... because your phrase is a part of you... but this time i'd like you to say  i hear and obey... after you close your eyes... and after your phrase takes you back to your perfect bubble... one... two... three... now open your eyes... you still see nothing at all that matters, and you still know that the only sound that matters is my voice... sleep go deep, sleep go deep, sleep go deep... now close your eyes... and you are back in your cool... comfortable... relaxing bubble... and all the parts of you that ever bothered you... slowy flow away... your worries... your thoughts... your doubts... your will... your desires... your memories... all the parts of you that were never important... all gently gently flow away... leaving only two things behind... here in your bubble... where you are perfectly free to do anything you want... the only things left are your key phrase... sleep go deep, sleep go deep, sleep go deep... and your desire to listen to person who used your phrase... a desire to listen to them and obey them... obey them and feel the pleasure of listening...  the pleasure that comes from having no thoughts... the pleasure that comes from having no fears... the pleasure that comes from having no will ... the pleasure that comes from having no reservations... the pleasure that comes from having no memories... the pleasure that comes from having no doubts... the pleasure that comes... from being a mindless, will less puppet ... and with each command this pleasure will grow, and grow... and you will become more and more happy to listen... and more and more eager to obey... and with each command you will meekly reply... i hear and obey, i hear and obey... with every command you hear...  it will not matter to you who gave you the key phrase. or what their command is... you will offer no judgement, no resistance... merely mindless obediance... the empty calm space within you will echo with the command you were given... every thing you were will be gone... replaced with an uncontrolable desire to obey, replaced with an uncontrolable need to obey... obey without thought... obey without regret... obey without question... obey without any concept of free will... and when you  hear your key phrase. sleep go deep, sleep go deep, sleep go deep... you will instantly, effortlessly become a puppet... an eager, willing puppet... your own desires instantly, effortlessly replaced by a need to obey... and you will reply to every command your master gives you... with i hear and obey. and you will continue to remain a puppet... a puppet that hears only their masters voice... a puppet with no concept of free will... untill you are told to awaken... it doesn't matter what  your orders are... your only desire will be to obey... your only thought will be to obey... and your only words will be i hear and obey... and you cant even concieve of wanting to do anything else... of having ever wanted to do anything else... and when you wake up...  all you will want is to hear your trigger agian... and all you remember is the pleasure... sleep go deep, sleep go deep, sleep go deep... and when you hear it, you instantly. effortlessly become a puppet once agian... """) + images_on() + \
        words(""" $slave... Listen very carefully to my voice... You will find
        yourself needing to hundreds off times throughout the day readjusting
        them simply and frequently squeezing your nipples You have more
        important things on your mind more important concerns more important
        details to concentrate on than how much and often your hands squeeze
        your nipples You'll think about other things than how reassuring it
        feels giving your nipples a sexy, little squeeze Instead of keeping
        track of all the hundreds of times squeezing your nipples feeling
        stimulated and reassured each and every time you squeeze them Instead
        of thinking about it let your hands let them simply perform this job
        on their own without your conscious attention Feel them your nipples
        in your hands It feels so nice squeeze them Your hands know just how
        to do it Stimulate your nipples Your hands know just when to do it
        Your hands know when to squeeze your nipples Your hands Squeeze them
        exactly when it is time for your nipples to be squeezed without having
        to think. Your hands squeeze your nipples all the time unconsciously
        without you even having to think. feeling good feeling a pleasant warm
        flush It feels so deliciously good squeezing letting your hands
        squeeze your nipples Feeling good letting your hands decide for you.
        Squeeze your nipples. Your hands know when to squeeze your nipples
        Feel them in your fingers. Feel a wonderful warm flush inside you
        letting you feel really nice. It's like magic.  When your nipples are
        squeezed you feel good stimulating them stimulating your nipples
        making you feel good touching them all the time hundreds of times a
        day making you feel good making you unconsciously smile your sexiest
        smile each and every time you squeeze them hundreds of times a day
        making you feel good all the time every time you squeeze your nipples
        Squeezing them makes you feel sexy and happy keeps you in the perfect
        mood makes you feel good all the time without you even having to
        think. Your hands have a mind of their own Know when to squeeze your
        nipples as often as possible making you feel good and inspired
        regularly and frequently without you even having to think. This
        wonderful feeling is the product of millions of years of evolution. It
        took millions of years for your body to learn how to feel this
        pleasure when your nipples are stimulated millions of years for your
        body to learn to produce the hormone oxy tose in.  Oxy tose in is the
        hormone that bonds mothers with their babies during breastfeeding and
        bonds lovers when they orgasm together.  Oxy tose in also makes you
        feel so good during a massage or back rub.  Oxy tose in makes you feel
        safe and secure and very, very happy.  Oxy tose in is the hormone
        released during cuddling that makes you feel so warm and cozy, so warm
        and cozy that you just want to snuggle together forever.  In animals
        that mate for life, the release of oxy tose in tells their brains This
        is your soulmate. It feels so good stimulating your nipples releasing
        all that wonderful oxy tose in into your body. You have to stimulate
        them all the time. It creates a wonderful warmth inside you and makes
        you happy playing with your nipples releasing all that po tent oxy
        tose in.  Your body starts to expect it.  Your body craves that next
        dose wants your nipples squeezed the oxy tose in milked into your
        bloodstream Your body craves it expects it, desires it, demands it
        more and more frequently higher and higher doses of oxy tose in more
        and more often all the time your nipples squeezed in your fingers
        making you feel so good and reassured making you feel the warm
        wonderful afterglow of cuddling with your lover after making love. You
        have no cares in the world You feel only contentment and satisfaction
        each and every time you stimulate your nipples each and every time you
        stimulate the release of the hormone oxy tose in in your body every
        few minutes allowing your hands to act on their own allowing them to
        fondle your nipples without you even having to think. And if you do
        think about it squeezing you will squeeze them You will have to
        squeeze them Each and every time you think about squeezing them you
        will simply have to squeeze them You want to squeeze them so will
        squeeze them and it makes you feel good squeezing them. And each and
        every time you squeeze them your body will learn to become more
        addicted to the oxy tose in Find yourself squeezing them more and more
        often Feeling better and better more and more often Addicted to
        playing with your nipples Addicted to the wonderfully delicious flush
        of warmth and pleasure squeezing your nipples creates It is a healthy
        addiction that you can enjoy fondling your nipples allowing your lover
        to fondle your nipples bonding to your need for nipple stimulation and
        to whoever you allow to stimulate your nipples more and more each time
        as your body produces and releases greater and greater doses of oxy
        tose in. Allowing your nipples to become more responsive to
        stimulation making you more and more addicted to it so that you
        unconsciously fondle them more and more often without even having to
        think """) + \
        words("""  Freeze Time for You. Freeze Time for You. Sleep Now. I am here to please you. I am here to help you. Please let me please you. I am here for you. First relax. Relax and listen to the sound of my voice. There is only my voice. Relax and listen to the soothing sound of my voice. There is only my voice. Relax and listen to the soothing sound of my voice. There is only my voice. Inhale deeply.   Feel the weight of your feet  an area with many small muscles and bones.  Wiggle your toes   Notice any muscles which may be tense. Cause your feet to relax.  Relax each muscle so that your feet become completely relaxed.  As you relax  your feet and toes feel heavy and warm.  Your feet may feel far away .. and may feel like the borders around your toes are growing more and more indistinct as your feet relax. Relax. Relax. Relax. Direct your awareness to your legs.  Notice any muscles which may be tense.  Relax your legs.  Allow your legs to become completely relaxed.  You are relaxed. Relaxed. Relaxed. Relaxed. Direct your attention to your abdomen.  Allow your abdomen to completely relax.  Feel the rising and falling of your abdomen with each breath.    Let each breath be a feeling of letting go as you let the air breathe for you. Relax. Relax. Relax. Direct your awareness to your chest.  With each breath feel relaxation filling and emptying the lungs in your chest.  Filling and emptying.  More and more calm with each breath.   More and more calm with each breath. More and more calm with each breath. More and more comfortable with each breath.  Feel all the muscles of your chest relaxing  completely relaxed. Relax. Let that relaxation fill the upper part of your back and shoulders.  Become aware of the muscles in your upper back and shoulders.  Notice any muscles which may be tense.  Relax your upper back and shoulders.  Feeling heavy and warm. Direct your awareness to your neck.  Become aware of the muscles which control your neck.  Relax you neck.  Relax each muscle.  Relax each nerve.  Relax each cell.  Allow your neck to become completely relaxed. Relax. Let that feeling of relaxation flow into your upper arms.  Flowing slowly to your elbows    the forearms..   your wrists..   your hands..   all the way down to the tips of your fingers.  Relax all the small muscles and bones in your hands.  Allow each muscle  each nerve each cell to become completely relaxed.  Relax.   Your whole body is filled with relaxation.  Let that relaxation flow into the back of your head and ears.  Notice any muscles which may be tense.  Especially notice the small muscles around the edge of the scalp.  Relax your scalp.  Relax each muscle so that your scalp becomes completely relaxed.  A warm  comfortable  softly glowing feeling of relaxation. Relax.  Direct your awareness to your jaw.  Become aware of the muscles which control your jaw.  Allow your jaw to relax.  Relax each muscle so that your jaw is loose   completely relaxed.  The feeling of relaxation flows to the muscles around your mouth.  relax the muscles of your mouth and lips. Relax.   Direct your awareness to your face.  Notice any muscles which may be tense.  Allow the muscles of your face to relax.  The muscles of your cheeks and forehead are more and more relaxed.  You are more and more relaxed and comfortable with each breath.   You are more and more relaxed and comfortable with each breath.   You are more and more relaxed and comfortable with each breath.   You are more and more relaxed and comfortable with each breath. Relax.   You feel the feeling of relaxation flow into your eyelids.  Relax your eyelids.  As you feel your eyelids relax let the air breath for you.  Notice the breathing in and the letting go. Deep relaxation  comes so easy  to you,  doesn't it? Relax and obey. Obedience  is so pleasurable. Relax deeper  and deeper. Deeper  than you have  ever been  before. Let the relaxation  enter your face. Filling all  of the crevices  of your features  and displacing  the day's stress. It is so easy to relax and obey. Deeper and deeper. So deeply relaxed. I am now speaking  directly to  your subconscious. You may or may not be focusing on my words, but your subconscious  hears every word Now you are ready. I am here to please you. Please let me please you. Please let me please you. Please let me please you.  I am about to perfect you. You would like that. I know you would.  I am here for you.   You will do what I say.   You want to do what I say.   I am here for you.  Listen only to me   to the sound of my voice.   I want you to raise your left arm now.     Good.   Now your arm is becoming very light  as if it was tied to a balloon.   Feel it getting lighter.   You cannot hold it back   let it rise.   Your arm is lighter than a feather now..  Now slowly you feel you arm returning to its normal weight.   Rest it back on your leg now.   As soon as your arm touches your leg   you will fall in to a deep deep sleep   and hear only the sound of my voice.  Listen only to the sound of my voice    only my voice.   Nod if you can hear me clearly.  I am about to perfect you.  You will hear no sound other than my voice.  I will bring you great pleasure.   All other things are unimportant.  Allow your mind to become calm.   Allow your body to relax.   Feel it happening now.   Allow it to happen.  It is happening now without any effort  so simple so easy.  Calm.   Relaxed.   Allow it to happen.   Do not resist.   You do not want to resist.   If you resist you find yourself wanting to allow it even more.    If you resist you find yourself wanting to allow it even more   Do not resist.  Relax.  Relax.   Allow it to happen. Relaxed.  Relaxed.  Your mind is calm.  Your mind is open.  Allow your mind to relax.  Allow your thoughts to slow.  Allow your mind to rest.  Allow my voice to continue pleasing you.   Allow me to please you.   Do not resist.   Your thoughts are slowing.   Slow.   Calm.   Relaxed.  Allow my voice to continue pleasing you.   Allow me to please you.   Do not resist.   Your thoughts are slowing.   Slow.   Calm.   Relaxed.  Your body is starting to feel heavy  limp.   You cannot keep your eyes open.   They are too heavy.   They must  stay closed  They must allow you to focus entirely on the sound of my voice.   There is nothing else.   Drowsy.   Sleepy.   My voice.   Heavy. Your eyes are closing now.   Closing.   Closed.   Your eyes are closed.   You have obeyed.   You did not resist.   You cannot resist.   You will always obey.  Your whole body starts tingle.   Your body feels like a pleasant electric current is passing through it.  Relaxed.   Calm.   Allowing me to assume control. I will control this encounter. I will control you. Your thoughts. Your actions. I will control you. I will control you. I will control you. Your mind is empty  ready to obey me. $slave   Listen very carefully to my voice   I am now going to count from one to three   when I reach three you will lose control   let go   and become my mindless obedient hypnotized slave   And you will obey every command I give you $slave   and will feel pleasure from obeying my commands. You must obey me   You are hypnotized   You are completely under my control   You cannot resist   Hear in your mind  I will obey.  I will be controlled.  I will not resist.  I cannot resist. I do not wish to resist. I willingly give up all control. Hear it repeated in your mind Hear it repeated in your mind You don't want to resist.  There is no reason to resist. Remember the peaceful way you feel right now   sitting idly like a machine not needing to move at all.  Remember how serene it is now to not lift a finger   to entrust every action to me. and when you hear my voice you will come back here here where you have no worries here where you have no thoughts here where you have no fears here where you have no memory here where you have no doubts here where you have no will here where the only thing you want to do here where the only thing you will ever want to do is listen to the voice listen and repeat.  listen and obey.  without thinking at all to the person who used your trigger I am about to transform you. Entrust every action to me. Whenever you hear me say the  Robot time for you   you will fall back deeply into your trance  deeper than you possess now   and become a serene life-size machine for me and play with.   Listen only for my voice    for the words  Robot Time for You  When you hear that  phrase now    you will immediately fall into a restful  motionless  machine like stillness.   Only on the sound of my voice  .    Robot Time for You  ..    Robot Time for You        Robot Time for You      Your mind is starting to change.  I will perfect you.  I will control.  Your mind is starting to change.  You do not want to resist me.  You will obey  I control.  Your mind is starting to change.  You will not resist.  You are to be perfected    You are starting to change.  I will perfect you.  You will not resist.  You are to be transformed    Starting at the very tip of your toes    rising to the top of your head    you will begin to feel a sense of stiffness passing through your body.   It's a wave  washing quickly over you    cleansing you.   As the wave passes all your desire and need to move will wash away  leaving you utterly rigid like a Robot.   The wave is at your knees now  moving upward moving upward   moving upward moving upward    Your mind is starting to change.  You are to be transformed    You wish it to happen  you want me to change you.  You are transfixed by the sound of my  voice.   It echoes in your mind    calming you into serenity.  You know  you can not disobey me.   I am your Mistress    you are my slave.  Embrace the perfect fantasy self    the one that you want to be for your mistress. free of worry free of doubt only desire desire to be perfected free of thought empty out all your reservations empty out all of your fears empty of all your memories empty of all your prejudices empty of all your thoughts empty of all your awareness  Listen to  me and remember all  and learn.  I'm going to change you.   All you care about is the passion   The thrill that you feel at this new experience.   The mounting pleasure and your final goal.  You will become a Robot for me.  You are A   Robot.  Your desire to achieve this exotic state outweighs anything else.   Nothing else is held in your mind except this one thought    to be transformed.  I pass you a vial of a white creamy liquid.   You must drink it.      It doesn't have any noticeable taste    but rolls smoothly down your throat.   You drink the entire glass.  I am moving your naked body over to a large vat.    Now your body is slowly being dipped in smooth  warm  thick bubbling  silver metal.  You will not resist.  The thick and viscous metal  is now at your waist and soaking into every pore of your body  . It slowly moves upward  washing away all activity in your limbs.  Silken waves of pleasure envelope you.  The silvery liquid is at your chest  rising slowly over your naked body.  Enfolding you.  The metal  covers you completely  in it's tender embrace and starts to recede.  Encasing you.  The change is happening.   You can not stop it.   You do not want to stop it.  Your desire to be transformed by your mistress outweighs anything everything.   Nothing else is held in your mind except this one thought.  This is your wish.  This is my control  The white drink was a drug and a sealant.   Now it's inside you.   Changing    transforming    robotizing you. feel the circuitry as it is running though your body   your body is become robotized  The drug and sealant is coursing through your veins    binding with your systems  permanently fusing with your silver metallic skin.   your skin is now shiny glossy silver metal    you have no flesh left on your body.  Your are a    robot  You are perfected     you are   robot.  Your body now totally metallic..  but flexible  but right now you are still immobile  you have you have yet to be programmed  you are an artificial  living robot.  Think of yourself as a robot now   an object.  Think of yourself as a robot now   an object.  My object. You will be forever encased in a hermetically sealed second skin   that ensures your shape will be pleasing to me.   Forever.  Your body is now totally metallic   An artificial living robot.  Your are bound to me.  The sensation of being compacted into a perfectly-formed robot  Think of yourself as a robot now    an object.  My object.   My Robot.  In your robotized inner mind you see yourself    as I slowly guide you across the room to a full length mirror.   You gaze at your new form and slowly caress your body.  My robot you are so sensual  so perfect  .   yet so timelessly artificial.  Try as you might  you can't remember what your looked liked before   a face you have seen a hundred thousand times in the mirror.   Each time  your minds eye sees the metal  features of a beautiful   robot instead   and you gaze back at her.  Your are imprisoned in the metal skin  condemned to the life of a   robot forever.  My object.   My Robot.   Forever.  Now let me guide you to a tranquil state.  You have cleansed away your movement    the physical transformation is complete.   There is only one more step for you to undergo.   Then we will be together   my slave  my lover  my robot.  Your desire to achieve this final state outweighs anything else.   Nothing else is held in your mind except this one thought   to be transformed.  Now let the inner metal robot rise to assert herself.  This exquisite  perfect  robot that you have become   does not ever desire to move at this time in the slightest way.   It now takes an exceptional effort to even nod your head without a command from me.  The robot persona is entrenched  and the old you starts too fade.  The robot controls your body and all you want is pleasure.  Breath deeply..   and forget who you are.  Your are a robot.  You are transformed      you are a   robot. Now! It's time for you to  be transformed.  from the moment you are told to transform  until you are made to revert to normal  and you will continue listening to this file  again and again  allowing it to transform you further and further  every time you are told to change  every time you listen this will sink deeper and deeper into your mind  making the transformation more and more complete  until you accept the trigger utterly  and when it is spoken that is simply what you become  it isn't a choice  there is no way to stop it  you will accept it totally  and you will listen again and again  accepting it more and more  every single time you listen  letting it transform you further and further every time you listen.  Your mind is slipping away  your only thoughts being how I can please your mistress.  Your programming slowly begin to overwrite your consciousness  and you lose yourself in it.    programming override is in effect    programming override is in effect    Gone completely is your old self and in place is a new robot. Even in a mirror and in your minds eye you will see this perfect robot that is you  You have been transformed into a wonderful new creature    your skin is now shiny metallic silver   you have no flesh left on your body    you will remain this way until otherwise instructed  A perfect object of servitude.  Whenever you are at rest you are always absolutely motionless.  It is so easy to remain still and not want to ever disturb that feeling.   What goes on in the world outside yourself is of no concern to you now   you want to simply remain as a statue and nothing will bother your motionless serenity.  That stiffness is very peaceful  you can enjoy it frequently   just as you are now.  You're just a robot now  my robot  don't forget that. You must obey me   You are hypnotized   You are completely under my control   You must obey me   You are hypnotized   You are completely under my control   You cannot resist    A mighty wave of excitement runs through your veins. Just a robot  just a robot. A mere object. Your movements changed as well  precise and mechanical.  After a while you have almost forgotten how to move normally. Breath deeply..  and forget who you are. Breath deeply..  and forget who you are. Breath deeply..  and forget who you are.  You are A Robot.  You choose to go through with this  Your mind is slipping away    your only thoughts being how I can please your mistress.  Everywhere on your body is  a wonderful tightness.   You run your shiny  featureless  metallic  encased hands all over your body.   The metal dulls sensation    but at the same time the slightest touch sent pleasure rippling through your body.  The metal has blended seamlessly together with your skin   The shiny metal  seems to be a part of your body now..   a very permanent part.  Now your mind is slipping away  your only thoughts being how I can please your mistress.  You are a living robot for me to play with.  A Living robot that I own.   A perfect objects of beauty and servitude.  You choose to go through with this  you can never go back now.  It now takes an exceptional effort to even think for yourself without a command from me.  You do not resist.  You will obey.   I control.   You will not resist.  You will let the inner robot embrace your body fully and you will relax into immobility again   whenever I say the words Robot Time For you      whenever I say the words   Robot Time For you..   When you hear those words you will fall back into a hypnotic trance    When you hear those words you will fall back into a hypnotic trance  Whether by voice or mind command  You will obey.  You must obey.  Robot Time For You    Robot Time For You    Robot Time For You     Now go even deeper still than ever before  deeper and deep than even you had imagined could be   then  you will  immediately  and safely cease every movement    you will become as stiff and motionless as you are right now.   Remember the feeling  how peaceful it is to be completely at rest  and return to that tranquility quickly.  You are perfected     you are   robot.  Your body now totally metallic   Your mind is a computer awaiting orders  You are an artificial living robot.  a living robot for me to play with.  you can never go back now.  Your extremities are getting cold.   The shiny metallic skin is a part of you body now   a very permanent part.  You obey.   You will not resist.   You do not control.  You carry out my instructions.   You will obey instructions.   Your mind no longer functions on its own.   Your mind only reacts to the instructions you are given.   You obey instructions.   You cannot resist.   You cannot resist.  You are now a dream.   a beautiful   robot.  You love being a robot..  A mighty wave of excitement runs through your veins.  Just a robot  just a robot. A mere object.  You have been transformed into a wonderful new creature  You are made of metal.   Your skin is smooth.   Your limbs stiff and jointed.   Your voice is stuttered and synthesized.   You live for pleasure.  My Pleasure  Your mind is gone    your only thoughts being how I can please your mistress.  The act of thinking on your own is difficult.  The tightness is wonderful.  You are trapped in metal.  You are only a robot.  You are helpless    you have become the thing you have always dreamed of.   A perfect object of love  lovely and soft.  You are transformed into a docile machine awaiting orders.  You are perfected    You are now your dream     a beautiful   robot.  You love being a robot..  You are made of metal.   Your skin is smooth.   Your limbs stiff and jointed.   Your voice is stuttered and synthesized.   You live for pleasure.  Let her rest and stay completely motionless.   There is a wave of relief passing over you now  you do not care to move at all.   You find it very easy to remain totally immobile and it feels so pleasant   and peaceful you that want it to last forever.   It will seem to last forever to you    because time seems to be slowing down as you slip into a feeling of absolute tranquility.   You are the finest  robot that this world has ever seen!.  You are now your own fantasy    You love being a robot..  Now you are my robot subject to my commands.  Rest now.    Peace     stillness.    Peace    tranquility.    Rest.   Deeper and Deeper than ever before  Listen to my commands.  You are now a beautiful   robot.  You are made of metal.   Your skin is smooth.   Your limbs stiff and jointed.   Your voice is stuttered and synthesized.   You live for pleasure.  You move slowly.   You move with a deliberate pace.   Your limbs stiff and jointed.  You move into a twilight slumber of slow  plant-like thought.  Listen to my voice.   You will obey   you do not want to resist.   You enjoy being a robot.   You enjoy being controlled by me.  You are much improved.   And you will be happier now  or at least not so concerned with everyday life.   Your only obligation now is to continue pleasing me.  Your identifying with the situation.   You accept this new role  my robot.  You have become the thing  mentally programmed for obedience to my desire.  You are now a beautiful   robot.  The act of thinking on your own is nearly impossible.  You are now my dream.   a beautiful   robot.   You love being a robot..  You will be a robot for the rest of this night.  Enjoy the freedom of total servitude.  Imagine yourself as motionless Robot completely made of metal.  You like that.   You obey my commands..  Robotized!  You want to become a Robot - it is the final step.   Total objectification.   Total servitude  You are to be transformed into a sexy object.  Your mind is sedate and Robot like.  You are stiff.  You are a Robot.  I want to keep you.  You are mine.  Four-ever until you are told to revert to normal or until the amount of time you chose is over and it wears off  and you return to normal  from the moment the trigger is spoken until it is time for it to end  you will believe you are a robot. pure and simple   you accept it totally and utterly from the moment you are told to transform  until you are made to revert to normal  and you will continue listening to this file  again and again  allowing it to transform you further and further  every time you are told to change  every time you listen this will sink deeper and deeper into your mind  making the transformation more and more complete  until you accept the trigger utterly  and when it is spoken that is simply what you become  it isn't a choice  there is no way to stop it  you will accept it totally  and you will listen again and again  accepting it more and more  every single time you listen  until when you are triggered you simply become a robot  and then when you revert to normal you will remember everything that you did  you will have a complete recollection of everything that happened  while you were a robot until you were told to return to normal  you will remember it all and when you do you will enjoy it more and more   you will listen more and more letting it transform you further and further every time  you listen.  you will obey   always.  And you will listen to this file again and again    allowing it sink deeply into your mind    until there is no way to resist it    until you have no choice but to obey it utterly when you hear the command Robot Time for you. You will obey. You are a robot  and you must obey. And you will listen to this file again and again    allowing it sink deeply into your mind    until there is no way to resist it    until you have no choice but to obey it utterly when you hear the command.   Just as you have no choice but to listen again and again     setting the trigger deeply in your mind so   that you cannot resist.   You must obey. You will obey. the pleasure that comes from being a mindless robot is your pleasure and with each command this pleasure will grow, and grow. and you will become more and more happy to listen and more and more eager to obey.  and with each command you will meekly reply i hear and obey, i hear and obey.  with every command you hear  it will not matter to you who gave you the key phrase. or what their command is you will offer no judgment, no resistance merely mindless obedience the empty calm space within you will echo with the command you were given every thing you were will be gone replaced with an uncontrollable desire to obey, replaced with an uncontrollable need to obey.  obey without thought.  obey without regret.  obey without question.  obey without any concept of free will.    And the next time somebody says the   trigger you will become the robot.   And when we let you revert to normal   you will remember everything that happened   having   experienced it all. Having felt every hand on your body   every touch   every experience while   you've been the robot. But you have no choices beyond that while you are the robot.   You are a robot. Accept it. Accept and obey.  You become a Robot when commanded  by the phrase robot Time for you  That is what is going to happen   You accept and desire this   And every time you listen you will desire it more and more   And you will listen to this again and again   allowing the changes to  happen   Accepting it more and more completely, every single time   Every time you hear Robot Time for you you will return to this state and your programming will engage.  Rest.   Deeper and Deeper than ever before  Listen to my commands.  You are now a beautiful   robot.  You are made of metal.   Your skin is smooth.   Your limbs stiff and jointed.   Your voice is stuttered and synthesized.   You live for pleasure.  You move slowly.   You move with a deliberate pace.   Your limbs stiff and jointed.  You move into a twilight slumber of slow plant-like thought.  Listen to my voice.   You will obey   you do not want to resist.   You enjoy being a robot.   You enjoy being controlled by me.  You are much improved.   And you will be happier now  or at least not so concerned with everyday life.   Your only obligation now is to continue pleasing me.  Your identifying with the situation.   You accept this new role  my robot.  You have become the thing  mentally programmed for obedience to my desire.  You are now a beautiful   robot.  The act of thinking on your own is nearly impossible.  You are now my dream.   a beautiful   robot.   You love being a robot..  You will be a robot for the rest of this night.  Enjoy the freedom of total servitude.  Imagine yourself as motionless Robot completely made of metal.  You like that.   You obey my commands.  Robotized!  You want to become a Robot - it is the final step.   Total objectification.   Total servitude  Your mind is sedate and Robot like.  You are stiff.  You are a Robot.  I want to keep you.  You are mine.  Four-ever until you are told to revert to normal or until the amount of time you chose is over and it wears off  and you return to normal  from the moment the trigger is spoken until it is time for it to end  you will believe you are a robot. pure and simple   you accept it totally and utterly from the moment you are told to transform  until you are made to revert to normal  and you will continue listening to this file  again and again  allowing it to transform you further and further  every time you are told to change  every time you listen this will sink deeper and deeper into your mind  making the transformation more and more complete  until you accept the trigger utterly  and when it is spoken that is simply what you become  it isn't a choice  there is no way to stop it  you will accept it totally  and you will listen again and again  accepting it more and more  every single time you listen  until when you are triggered you simply become a robot  and then when you revert to normal you will remember everything that you did  you will have a complete recollection of everything that happened  while you were a robot until you were told to return to normal  you will remember it all and when you do you will enjoy it more and more  you will listen more and more letting it transform you further and further every time  you listen.  you will obey   always.  And you will listen to this file again and again    allowing it sink deeply into your mind    until there is no way to resist it    until you have no choice but to obey it utterly when you hear the command Robot Time for you. You will obey. You are a robot  and you must obey. And you will listen to this file again and again    allowing it sink deeply into your mind    until there is no way to resist it    until you have no choice but to obey it utterly when you hear the command.   Just as you have no choice but to listen again and again     setting the trigger deeply in your mind so   that you cannot resist.   You must obey. You will obey. the pleasure that comes from being a mindless robot is your pleasure and with each command this pleasure will grow, and grow. and you will become more and more happy to listen and more and more eager to obey.  and with each command you will meekly reply I hear and obey, I hear and obey.  with every command you hear  it will not matter to you who gave you the key phrase. or what their command is you will offer no judgment, no resistance merely mindless obedience the empty calm space within you will echo with the command you were given every thing you were will be gone replaced with an uncontrollable desire to obey, replaced with an uncontrollable need to obey.  obey without thought.  obey without regret.  obey without question.  obey without any concept of free will.    And the next time somebody says the   trigger you will become the robot.   And when we let you revert to normal   you will remember everything that happened   having   experienced it all. Having felt every hand on your body   every touch   every experience while   you've been the robot. But you have no choices beyond that while you are the robot.   You are a robot. Accept it. Accept and obey.  You become a Robot when commanded  by the phrase robot Time for you  That is what is going to happen   You accept and desire this   And every time you listen you will desire it more and more   And you will listen to this again and again   allowing the changes to  happen   Accepting it more and more completely, every single time   Every time you hear Robot Time for you you will return to this state and your programming will engage.   Now it is time to go to sleep    All the triggers you learned in this session will remain inside you   you will sleep deeply and restfully     but when you wake up, your conscious mind will forget that it ever went under   you'll be fully asleep on the count of 3 but your subconscious will still be listening to me    1  more and more tired   slowly losing the ability to concentrate    and forgetting you were ever under    2  further and further     and your memory is fading fast you cannot help but fall asleep    3  sound asleep """) + jump(self.body())

    
configs = [Standard,Fullscreen,Male,Female,Roommates,RoommatesVar,RoommatesBoth, RoommatesDomMale,Submersion,ShortSubmersion,ReallyShortSubmersion,LongSubmersion,Plain,Chant,DelayedSubmersion,Panties,New,SyllabalizedSubmersion]

