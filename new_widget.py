# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:50:44 2020

@author: yaoyizhou
"""

from PyQt5 import QtCore, QtGui, QtWidgets
 
class Textbench:
    formula_dic={
            '0': "normal mode",
            '1': "calculas mode",
            '2': "set mode",
            '3': "latter mode",
            '4': "relation mode",
            '5': "function mode",            
            }
    caculas_dic={
            '0': r"\prime",
            '1': r"\int",
            '2': r"\iint",
            '3': r"\iiint",
            '4': r"\oint",
            '5': r"\lim",
            '6': r"\infty",
            '7': r"\nabla",
            '8': r"\mathrm{d}",
            '9': r"\partial",
            '10': r"\dot x",
            '11': r"\ddot y",
             
            }
    set_dic={
            '0': r"\emptyset",
            '1': r"\in",
            '2': r"\notin",
            '3': r"\subset",
            '4': r"\subseteq",
            '5': r"\supseteq",
            '6': r"\bigcap",
            '7': r"\bigcup",
            '8': r"\bigvee",
            '9': r"\bigwedge",
            '10': r"\biguplus",
            #'11': r"\bigsqcup",
            }
    latter_dic={
            '0': r"\alpha",
            '1': r"\beta",
            '2': r"\gamma",
            '3': r"\delta",
            '4': r"\omega",
            '5': r"\epsilpn",
            '6': r"\zeta",
            '7': r"\eta",
            '8': r"\theta",
            '9': r"\iota",
            '10': r"\kappa",
            '11': r"\lambda",
            '12': r"\mu",
            '13': r"\nu",
            '14': r"\xi",
            '15': r"\omicron",
            '16': r"\pi",
            '17': r"\rho",
            '18': r"\sigma",
            '19': r"\tau",
            '20': r"\upsilon",
            '21': r"\phi",
            '22': r"\chi",
            '23': r"\psi"
            }
    relation_dic={
            '0': r"\pm",
            '1': r"\times",
            '2': r"\div",
            '3': r"\mid",
            '4': r"\nmid",
            '5': r"\cdot",
            '6': r"\circ",
            '7': r"\ast",
            '8': r"\bigodot",
            '9': r"\bigotimes",
            '10': r"\bigoplus",
            '11': r"\leq",
            '12': r"\geq",
            '13': r"\neq",
            '14': r"\approx",
            '15': r"\equiv",
            '16': r"\sum",
            '17': r"\prod",                        
            }
    func_dic={
            '0': r"\log",
            '1': r"\lg",
            '2': r"\ln",
            '3': r"\bot",
            '4': r"\angle",
            '5': r"\sin",
            '6': r"\cos",
            '7': r"\tan",
            '8': r"\cot",
            '9': r"\sec",
            '10': r"\csc",
            '11': r"\arctan",
            '12': r"\arcsin",
            '13': r"\arccos",                                                
            }
    def trans_to_latex(self,mode_id,code_id):                
        if mode_id == 1:
            return self.clculas_dic[code_id]
        elif mode_id == 2:
            return self.set_dic[code_id]
        elif mode_id == 3:
            return self.latter_dic[code_id]
        elif mode_id == 4:
            return self.relation_dic[code_id]
        elif mode_id == 5:
            return self.func_dic[code_id]
        else:
            return ""
    
    
    
