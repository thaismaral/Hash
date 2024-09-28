# Hash

This repository contains the implementation of a user authentication and registration application using the SHA-256 hash algorithm, as well as the development of a brute force attack to crack passwords and the implementation of a solution to mitigate this type of attack.

Hash 1: User Registration and Authentication
• The application allows user registration and authentication.
• Each user has the following attributes:

Name: 4-character string.
Password: 4-character string.
• The registered user information is stored in a file in .txt, .csv, .json, or .xml format.
• The SHA-256 algorithm is used to hash the passwords before storing them.
Hash 2: Brute Force Attack with SHA-256
• The program processes the file containing the stored passwords and attempts to crack the password hashes using a brute force algorithm.
• The total time and the average time per password are calculated during the attack on 4 users.

Hash 3: Mitigation Against Brute Force Attack
• A solution was implemented to reduce the possibility of success in a brute force attack on the program developed in Hash 1. The solution may include adding salt, limiting login attempts, or using more robust algorithms.

*This program was made for the Information Security course in the third semester of Information Systems.*
