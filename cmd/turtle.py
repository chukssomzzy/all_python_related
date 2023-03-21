#!/usr/bin/env python3
import cmd, sys
from turtle import *


class TurtleShells(cmd.Cmd):
    intro = "Welcome to tge turtle shell.   Type help or ? to list commands.\n"
    prompt = "(turtle) "
    file = None

    def do_forward(self, arg):
        """Move the turtle forward by the specified distance: FORWARD 10"""
        forward(*turtle_parse(arg))
    def do_right(self, arg):
        """Turn turtle right by given number of degree: RIGHT 20"""
        right(*turtle_parse(arg))
    def do_left(self, arg):
        """Turn turtle left by given number of degrees: LEFT 90"""
        left(*turtle_parse(arg))
    def do_goto(self, arg):
        """Move turtle to an absolute position with changing orientation."""
        goto(*parse(arg))
    def do_home(self, arg):
        """Return turtle to the home position: HOME"""
        home()
    def do_circle(self, arg):
        """Draw circle with givem radius an options extent and steps: CIRCLE 50"""
        circle(*turtle_parse(arg))
    def do_position(self, arg):
        """Print the current turtle position: POSITION"""
        print("Current position is %d %d\n" % position())
    def do_heading(self, arg):
        """Print the current turtle heading in degrees: HEADING"""
        print("Current heading is %d\n" %(heading(),))
    def do_color(self, arg):
        "set the color: COLOR BLUE"
        color(arg.lower())
    def do_undo(self, arg):
        """Undo (repeatedly) the last turtle action(s): UNDO"""
    def do_reset(self, arg):
        """Clear the screen and return turtle to center: RESET"""
        reset()
    def do_bye(self, arg):
        """stop recording, close the turtle window, and exit: BYE"""
        print("Thank you for using Turtle")
        self.close()
        bye()
        return True

    """Record and playback"""
    def do_record(self, arg):
        """save future commands to filename: RECORD rose.cmd"""
        self.file = open(arg, "w")
    def do_playback(self, arg):
        """Playback commands from a file: PLAYBACK rose.cmd"""
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and  "playback" not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def turtle_parse(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    return tuple(map(int, arg.split()))

if __name__ == "__main__":
    TurtleShells().cmdloop()
