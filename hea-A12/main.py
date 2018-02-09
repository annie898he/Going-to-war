#-------------------------------------------------------------------------------
# Assignment: A12: Stacks, Queues, and the Card Game War
# Class:      CSC 236
# Name:       main.py
# Purpose:    To have two players show their top card, and the larger card wins
#             and gets place in the winning card's player's stack.
#             The player to have all the cards in their stack wins.
#
# Author:   Example stack and queue classes by Dr. Jan
#           Completed by Annie He (hea)
#
# Acknowledgments: Debugging help by Cody Myers
#
# Created:  16/10/2016
#-------------------------------------------------------------------------------

from war import War

def main():
    objectofwar = War()
    objectofwar.add_dealing()
    objectofwar.deal()
    objectofwar.make_move()

main()