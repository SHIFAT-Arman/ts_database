<p><a target="_blank" href="https://app.eraser.io/workspace/ayRUHZc5SNHfxrXE15oN" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

![ER Diagram](/.eraser/ayRUHZc5SNHfxrXE15oN___Sw74nJbVClclCggBhR055he503h2___---figure---kUCKQf_sBqqst4LEQrCd3---figure---LE_m70L-GTY6KwosprIAgA.png "ER Diagram")

> **Normalization**

1. completes
    1. UNF(UN-Normal Form) : c_email, c_name, c_id, c_phoneNum, c_dob, c_age, t_date, fees, amount, t_id
    2. 1NF (one-normal-form):  c_id,  t_id, c_email, c_name, , c_phoneNum, c_dob, c_age, t_date, fees, amount
    3. 2NF (two-normal-form): 
        1.  c_email, c_name, c_id, c_phoneNum, c_dob, c_age
        2. t_id, t_date, fees, amount, c_id(FK) 
    4. 3NF (three-normal-form): Same as 2NF
    5. BCNF (Boyce-codd-normal-form): Same as 2NF
2. uses
    1. UNF: fees, t_date, t_id, amount, m_id, m_email, m_name, bus_name, reg_date.
    2. 1NF: t_id, m_id, fees, t_date, amount,  m_email, m_name, bus_name, reg_date.
    3. 2NF: 
        1. t_id, t_date, fees, amount
        2. m_id, m_email, m_name, bus_name, reg_date, t_id (FK)
        3. 
    4. 3NF: same as 2NF
3. operates
    1. UNF: t_date, fees, amount, t_id, a_email, a_name, a_id, p_name, p_id
    2. 1NF: t_id, a_id, p_id, t_date, fees, amount, a_email, a_name, p_name
    3. 2NF: 
        1. t_id, fees, amount, t_date
        2. a_id, p_id a_name, a_email, t_id(FK), p_name
    4. 3NF: same as 2NF




<!--- Eraser file: https://app.eraser.io/workspace/ayRUHZc5SNHfxrXE15oN --->