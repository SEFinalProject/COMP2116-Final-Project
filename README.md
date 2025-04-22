# COMP2116-Final-Project
#The type of software development process:Agile
#Reason to choose:
#1.Flexible requirement changes: The initial core requirements are clear (movement, collision detection, scoring), but frequent adjustments to details (speed control, U optimization) are required during the development process
#2.Small team collaboration: 3-person teams can iterate quickly and synchronize progress on a daily basis
#3.Short term delivery verification: Complete a runnable version every week (including basic logic, interface optimization, and feature expansion)
#4.The waterfall model is not applicable: the requirements are fixed and the stages are strict, making it difficult to adapt to the rapid iteration requirements of course projects

#Usage:
#1.Main users: casual gamers, programming learners
#2.Usage scenario:
##1)Educational purpose: To demonstrate event driven programming and collision detection algorithms
##2)Entertainment use: Lightweight desktop games, suitable for fragmented time

#Development Process
#stage                              deliverables                              gongxian/technology
#requirement analysis               Function List (Mobile, Scoring, etc.)     Markdown document
#design                             Class diagram, flowchart                  Draw.io
#code                               Runnable core logic                       Python + Pygame
#test                               Bug fix record                            PyCharm Debugging Tool
#deploy                             GitHub repository+executable files        GitHub Actions

#Loran:Core Development - Mobile Logic, Collision Detection
#Carl:Testing and Optimization - Writing Test Cases, Performance Optimization
#Jim:Document and Interface Design - Writing Documents, UI Design, and Creating Presentation Videos

#Schedule
#weeks                                        milestone                                        detailed tasks
#1                                            Requirement analysis and prototype design        Determine game rules and draw U-sketches
#2                                            Implementation of core functions                 Complete snake movement, collision detection, and scoring logic
#3                                            Testing and Optimization                         Fix boundary bugs, optimize control response speed
#4                                            Documents and Delivery                           Record demonstration video and submit to GitHub repository

#Current State
#Completed function:
#1.Direction keys control movement 0
#2.Apple Generation and Scoring 0
#3.Boundary collision detection
#Features to be improved:
#1.Self collision detection (currently not implemented)
#2.Sound effect support

#Future Plan
#function                              priority                              person in charge                              implementation plan
#Difficulty classification             High                                  Carl                                          Add speed selection menu (FPS control)
#Archive/Read Files                    Medium                                Loran                                         Save game status using JSON
#Multi-Language Support                Low                                   Jim                                           Add a Chinese English switch button
