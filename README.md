<p><a target="_blank" href="https://app.eraser.io/workspace/ayRUHZc5SNHfxrXE15oN" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

[﻿ER Diagram](https://app.eraser.io/workspace/ayRUHZc5SNHfxrXE15oN?elements=LE_m70L-GTY6KwosprIAgA) 

## Normalization
1. completes
    1. UNF(UN-Normal Form) : c_email, c_name, c_id, c_phoneNum, c_dob, c_age, t_date, fees, amount, t_id
    2. 1NF (one-normal-form):  c_id,  t_id, c_email, c_name, , c_phoneNum, c_dob, c_age, t_date, fees, amount
    3. 2NF (two-normal-form): 
        1.  c_email, c_name, c_id, c_phoneNum, c_dob, c_age
        2. t_id, t_date, fees, amount, c_id(FK) 
    4. 3NF (three-normal-form): Same as 2NF
    5. BCNF (Boyce-codd-normal-form): Same as 2NF
2. uses
    1. UNF(UN-Normal Form): fees, t_date, t_id, amount, m_id, m_email, m_name, bus_name, reg_date.






<!--- Eraser file: https://app.eraser.io/workspace/ayRUHZc5SNHfxrXE15oN --->