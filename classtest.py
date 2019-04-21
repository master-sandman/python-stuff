#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class MyClass(object):
    myvar = "I was created at class level."
    
    def __init__(self):
        print("---Begin of constructor---")
        print(">>> MyClass.myvar: %s" % MyClass.myvar)
        print(">>> self.myvar: %s" % self.myvar)
        print("Change self.myvar...")
        self.myvar = "I'm a new property, am I?"
        print(">>> MyClass.myvar: %s" % MyClass.myvar)
        print(">>> self.myvar: %s" % self.myvar)
        print("Change MyClass.myvar...")
        MyClass.myvar = "I'm a class variable!"
        print(">>> MyClass.myvar: %s" % MyClass.myvar)
        print(">>> self.myvar: %s" % self.myvar)
        print("---End of constructor---")
    
    def __del__(self):
        print("---Begin of destructor")
        print(">>> MyClass.myvar: %s" % MyClass.myvar)
        print(">>> self.myvar: %s" % self.myvar)
        print("Change self.myvar...")
        self.myvar = "My time has come... :("
        print(">>> MyClass.myvar: %s" % MyClass.myvar)
        print(">>> self.myvar: %s" % self.myvar)
        print("Change MyClass.myvar...")
        MyClass.myvar = "Am I still alive?"
        print(">>> MyClass.myvar: %s" % MyClass.myvar)
        print(">>> self.myvar: %s" % self.myvar)
        print("---End of destructor---")

    def tellme(self):
        print(">>> self.myvar: %s" % self.myvar)

    @staticmethod
    def statictellme():
        print(">>> MyClass.myvar: %s" % MyClass.myvar)

if __name__ == '__main__':
    print("Getting started...")
    print("No object created, yet.")
    print("Let's call MyClass.tellme()")
    try:
        MyClass.tellme()
    except:
        print("<!> Nope. This doesn't work.")
    print("Okay, so let's call MyClass.statictellme()")
    try:
        MyClass.statictellme()
    except:
        print("<!> Nope. This doesn't work.")
    print("Fine. Let's create an object now.")
    myobj = MyClass()
    print("And again: let's call MyClass.tellme()")
    try:
        MyClass.tellme()
    except:
        print("<!> Nope. This doesn't work.")
    print("And again: let's call MyClass.statictellme()")
    try:
        MyClass.statictellme()
    except:
        print("<!> Nope. This doesn't work.")
    print("But we've got an object, so why don't use this?")
    print("Let's call myobj.tellme()")
    try:
        myobj.tellme()
    except:
        print("<!> Nope. This doesn't work.")
    print("And then let's call myobj.statictellme()")
    try:
        myobj.statictellme()
    except:
        print("<!> Nope. This doesn't work.")
    print("So far so good. Let's delete the object.")
    del myobj
    print("Could we still call myobj.tellme()?")
    try:
        myobj.tellme()
    except:
        print("<!> Nope. This doesn't work.")
    print("I promise, this is the last time we call MyClass.statictellme()")
    try:
        MyClass.statictellme()
    except:
        print("<!> Nope. This doesn't work.")
    print("Yes, it seems.")
    print("Okay, that's it. Over and out!")