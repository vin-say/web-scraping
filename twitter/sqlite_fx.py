# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:12:12 2019

@author: Vincent Sayseng

Scripts were adopted from the SQLite Python Tutorial
http://www.sqlitetutorial.net/sqlite-python/
"""
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    return None

def add_follower_game_rev(conn, profile):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """
#    sql = ''' INSERT OR REPLACE INTO profiles(id,screen_name,location,friend_count)
#              VALUES(?,?,?,?) '''
    sql = ''' INSERT INTO game_rev_followers(
                id, id_string, name, screen_name, location,
                url, description, protected, verified, followers_count,
                friend_count, listed_count, favourites_count, 
                statuses_count, created_at, default_profile,
                default_profile_image)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.executemany(sql, profile)
    return cur.lastrowid

def add_follower_ustwo(conn, profile):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """
#    sql = ''' INSERT OR REPLACE INTO profiles(id,screen_name,location,friend_count)
#              VALUES(?,?,?,?) '''
    sql = ''' INSERT OR REPLACE INTO ustwo_followers(
                id, id_string, name, screen_name, location,
                url, description, protected, verified, followers_count,
                friend_count, listed_count, favourites_count, 
                statuses_count, created_at, default_profile,
                default_profile_image)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.executemany(sql, profile)
    return cur.lastrowid

def add_follower_playdead(conn, profile):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """
#    sql = ''' INSERT OR REPLACE INTO profiles(id,screen_name,location,friend_count)
#              VALUES(?,?,?,?) '''
    sql = ''' INSERT OR REPLACE INTO playdead_followers(
                id, id_string, name, screen_name, location,
                url, description, protected, verified, followers_count,
                friend_count, listed_count, favourites_count, 
                statuses_count, created_at, default_profile,
                default_profile_image)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.executemany(sql, profile)
    return cur.lastrowid

def add_follower_that_game_comp(conn, profile):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """
#    sql = ''' INSERT OR REPLACE INTO profiles(id,screen_name,location,friend_count)
#              VALUES(?,?,?,?) '''
    sql = ''' INSERT OR REPLACE INTO that_game_comp_followers(
                id, id_string, name, screen_name, location,
                url, description, protected, verified, followers_count,
                friend_count, listed_count, favourites_count, 
                statuses_count, created_at, default_profile,
                default_profile_image)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.executemany(sql, profile)
    return cur.lastrowid

def add_follower_rusty_lake(conn, profile):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """
#    sql = ''' INSERT OR REPLACE INTO profiles(id,screen_name,location,friend_count)
#              VALUES(?,?,?,?) '''
    sql = ''' INSERT OR REPLACE INTO rusty_lake_followers(
                id, id_string, name, screen_name, location,
                url, description, protected, verified, followers_count,
                friend_count, listed_count, favourites_count, 
                statuses_count, created_at, default_profile,
                default_profile_image)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.executemany(sql, profile)
    return cur.lastrowid

def add_follower_ids_ustwo(conn, profile_id):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """

    sql = ''' INSERT INTO ustwo_followers_ids(id) VALUES(?) '''

    cur = conn.cursor()
    cur.executemany(sql, profile_id)
    return cur.lastrowid

def add_friends_ids_game_rev(conn, ids):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """

    sql = ''' INSERT INTO game_rev_friends_ids(user_id, friend_id) 
                VALUES(?,?) '''

    cur = conn.cursor()
    cur.executemany(sql, ids)
    return cur.lastrowid

def add_friends_ustwo_game_clust(conn, ids):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """

    sql = ''' INSERT INTO ustwo_game_clust_friends_ids(user_id, friend_id) 
                VALUES(?,?) '''

    cur = conn.cursor()
    cur.executemany(sql, ids)
    return cur.lastrowid

def add_friends_ustwo_sampled(conn, ids):
    """
    Create a new project into the projects table
    :param conn:
    :param profile:
    :return: profile id
    """

    sql = ''' INSERT INTO ustwo_sampled_friends_ids(user_id, friend_id) 
                VALUES(?,?) '''

    cur = conn.cursor()
    cur.executemany(sql, ids)
    return cur.lastrowid


def add_gr_fol_friend(conn, profile):
    
    sql = ''' INSERT OR REPLACE INTO game_rev_fol_friends(
                id, id_string, name, screen_name, location,
                url, description, protected, verified, followers_count,
                friend_count, listed_count, favourites_count, 
                statuses_count, created_at, default_profile,
                default_profile_image, popularity_count)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, profile)
    return cur.lastrowid

def add_ustwo_game_clust_fol_friend(conn, profile):
    
    sql = ''' INSERT OR REPLACE INTO ustwo_game_clust_fol_friends(
                id, id_string, name, screen_name, location,
                url, description, protected, verified, followers_count,
                friend_count, listed_count, favourites_count, 
                statuses_count, created_at, default_profile,
                default_profile_image, popularity_count)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, profile)
    return cur.lastrowid
    
def add_ustwo_sampled_fol_friend(conn, profile):
    
    sql = ''' INSERT OR REPLACE INTO ustwo_sampled_fol_friends(
                id, id_string, name, screen_name, location,
                url, description, protected, verified, followers_count,
                friend_count, listed_count, favourites_count, 
                statuses_count, created_at, default_profile,
                default_profile_image, popularity_count)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, profile)
    return cur.lastrowid