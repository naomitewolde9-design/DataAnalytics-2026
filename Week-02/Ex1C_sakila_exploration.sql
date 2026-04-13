/*
a) When you expand Table/actor and expand collumns the list underneath includes "actor_id", "first_name", "last_name", "last_update".
b) When you expand Table/actor and expand collumns the list underneath includes film, title, description, release_year, language_id, 
original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update .
c) The tables that have actor_id and film_id in the collumns is the actor table, film table, film_actor table, film_category table,
 film_text table, and inventory table 
 d) The rental table did appear in a sepreate file tab in SQL and it showed a table with the logs of the people who rented stuff, what exactly 
 they rented, staff id, and the return information. This was not hard to read once I really looked into it because everything is organized. I think 
 the only thing that was hard to read was the inventory id. I don't know what exactly people are renting. 
 e) The Inventory table appeared in a sepreate file and showed the inventory number and the store number and how much of that item is listed in the inventory.
 It was easier to read when I actually thought about what the data was trying to say. 
 f) To understand the tables given you need to locate the store id, customer id, time stamps with the dates and time included. Everything needs to be in the proper order so that the data tells the story.
 For example having the store id(where), rental date(when they reiceved item), return date etc. 
 */
 
 SELECT * FROM rental; -- retrieved 1001 records 
 
 SELECT * FROM inventory; -- retrieved 1000 records 