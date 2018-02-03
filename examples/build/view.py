#!usr/bin/python
# -*- coding: cp1252 -*-
# This is the view2 module for Python.
# © Copyright 2018-2025 Mhamad Alsukairy. All rights Reserved.
import pygame
RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
X_AXIS = "x"
Y_AXIS = "y"
class ViewPort:
    def __init__(self, netX, netY):
        self.obj_data = []
        self.pin = -1
        self.disabled = False
        self.netX = netX
        self.netY = netY
    def __str__(self):
        msg = "view.ViewPort class object."
        return msg
    def addObj(self, x_pos_r, y_pos_r, direction):
        self.obj_data.append([x_pos_r, y_pos_r, direction])
        self.pin += 1
        return self.pin, [x_pos_r, y_pos_r]
    def changeDirection(self, new_direction):
        #self.obj_data[pin][2] = new_direction
        a = 0
        for a in range(len(self.obj_data)):
            self.obj_data[a][2] = new_direction
        return new_direction
    def stopMotion(self):
        a = 0
        for a in range(len(self.obj_data)):
            self.obj_data[a][2] = None
        return "Motion has been stopped"
    def getX(self, pin): return self.obj_data[pin][0]
    def getY(self, pin): return self.obj_data[pin][1]
    def getCords(self, pin):
        return self.obj_data[pin][0], self.obj_data[pin][1]
    def getNetX(self): return self.netX
    def getNetY(self): return self.netY
    def setX(self, pin, new_x):
        self.obj_data[pin][0] = new_x
        return self.obj_data[pin][0]
    def setY(self, pin, new_y):
        self.obj_data[pin][1] = new_y
        return self.obj_data[pin][1]
    def setCords(self, pin, newCords):
        self.obj_data[pin][0] = newCords[0]
        self.obj_data[pin][1] = newCords[1]
    """def addX(self, pin, add_num):
        self.obj_data[pin][0] += add_num
        return self.obj_data[pin][0]
    def addY(self, pin, add_num):
        self.obj_data[pin][1] += add_num
        return self.obj_data[pin][1]
    def subX(self, pin, sub_num):
        self.obj_data[pin][0] -= sub_num
        return self.obj_data[pin][0]
    def subY(self, pin, sub_num):
        self.obj_data[pin][1] -= sub_num
        return self.obj_data[pin][1]"""
    def getDirection(self): return self.obj_data[0][2]
    def disable(self): self.disabled = True
    def enable(self): self.disabled = False
    def updateStats(self, by):
        """Use this func to move the players surroundings.
which will create the signature view effect!"""
        if not self.disabled:
            a = 0
            if self.obj_data[0][2] == "right":
                a = 0
                self.netX += by
                for a in range(len(self.obj_data)):
                    self.obj_data[a][0] -= by
            elif self.obj_data[0][2] == "left":
                a = 0
                self.netX -= by
                for a in range(len(self.obj_data)):
                    self.obj_data[a][0] += by
            elif self.obj_data[0][2] == "up":
                a = 0
                self.netY -= by
                for a in range(len(self.obj_data)):
                    self.obj_data[a][1] += by
            elif self.obj_data[0][2] == "down":
                a = 0
                self.netY += by
                for a in range(len(self.obj_data)):
                    self.obj_data[a][1] -= by
    def updateCustomStats(self, pin, by):
        if not self.disabled:
            if self.obj_data[pin][2] == "right":
                self.obj_data[pin][0] -= by
            elif self.obj_data[pin][2] == "left":
                self.obj_data[pin][0] += by
            elif self.obj_data[pin][2] == "up":
                self.obj_data[pin][1] += by
            elif self.obj_data[pin][2] == "down":
                self.obj_data[pin][1] -= by
"""    def updatePlayerPos(self, direction, by):
        Don't worry about this func if you are not
making a multiplayer game.
        if not self.disabled:
            if direction == "right":
                self.netX += by
            elif direction == "left":
                self.netX -= by
            elif direction == "up":
                self.netY -= by
            elif direction == "down":
                self.netY += by"""
