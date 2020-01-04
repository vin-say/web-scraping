"""
Created on Fri Jun  7 02:33:53 2019

@author: Vincent S

Script to pull follower data off Twitter and stores in SQL database
"""

import tweepy
import json
import pandas as pd
import os
import sqlite_fx
from time import sleep

# %% Twitter API app keys and tokens

from gr_analyst_keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

# %% Function definitions

def pull_user_data( users ):
    # Pulls user data from the Tweepy user object and arranges it to tabular format for SQL
    
    try:
        # check if users is iterable
        iter(users)
    except TypeError:
        # integer (int64) representation of unique identifier for user
        id_int = users._json['id']
        # string representation of unique identifier for user
        id_str = users._json['id_str']
        # name (string) of user as they've defined it
        name = users._json['name']
        # screen name (string) or handle of user
        screen_name = users._json['screen_name']
        # user-defined location (string), nullable
        location = users._json['location']
        # URL (string) provided by user in association with profile, nullable
        url = users._json['url']
        # user-defined description (string) of profile, nullable
        description = users._json['description']
        # protected status (bool)
        protected = users._json['protected']
        # verified status (bool)
        verified = users._json['verified']
        # number (int) of followers user has
        followers_count = users._json['followers_count']
        # number (int) of accounts user follows
        friend_count = users._json['friends_count']
        # number (int) of public lists user is member of
        listed_count = users._json['listed_count']
        # number (int) of tweets user has liked
        favourites_count = users._json['favourites_count']
        # number (int) of tweets and retweets issued by user
        statuses_count = users._json['statuses_count']
        # UTC date and time user account was created (string)
        created_at = users._json['created_at']
        # whether user has not altered the default theme or background (bool)
        default_profile = users._json['default_profile']
        # wheter user has not uploaded their own profile image
        default_profile_image = users._json['default_profile_image']
        # compile profile parameters as one ouput
        profile = [id_int, id_str, name, screen_name, location, url,
                           description, protected, verified, followers_count,
                           friend_count, listed_count, favourites_count,
                           statuses_count, created_at, default_profile, 
                           default_profile_image]
    else:
        # integer (int64) representation of unique identifier for user
        id_int = [user._json['id'] for user in users]
        # string representation of unique identifier for user
        id_str = [user._json['id_str'] for user in users]
        # name (string) of user as they've defined it
        name = [user._json['name'] for user in users]
        # screen name (string) or handle of user
        screen_name = [user._json['screen_name'] for user in users]
        # user-defined location (string), nullable
        location = [user._json['location'] for user in users]
        # URL (string) provided by user in association with profile, nullable
        url = [user._json['url'] for user in users]
        # user-defined description (string) of profile, nullable
        description = [user._json['description'] for user in users]
        # protected status (bool)
        protected = [user._json['protected'] for user in users]
        # verified status (bool)
        verified = [user._json['verified'] for user in users]
        # number (int) of followers user has
        followers_count = [user._json['followers_count'] for user in users]
        # number (int) of accounts user follows
        friend_count = [user._json['friends_count'] for user in users]
        # number (int) of public lists user is member of
        listed_count = [user._json['listed_count'] for user in users]
        # number (int) of tweets user has liked
        favourites_count = [user._json['favourites_count'] for user in users]
        # number (int) of tweets and retweets issued by user
        statuses_count = [user._json['statuses_count'] for user in users]
        # UTC date and time user account was created (string)
        created_at = [user._json['created_at'] for user in users]
        # whether user has not altered the default theme or background (bool)
        default_profile = [user._json['default_profile'] for user in users]
        # wheter user has not uploaded their own profile image
        default_profile_image = [user._json['default_profile_image'] for user in users]
        # Zip together profile parameters into list
        profile = list(zip(id_int, id_str, name, screen_name, location, url,
                           description, protected, verified, followers_count,
                           friend_count, listed_count, favourites_count,
                           statuses_count, created_at, default_profile, 
                           default_profile_image))
    
    return profile
    
# %% Access twitter API via Tweepy
    
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# %% sqlite shadows slumber

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_follower_game_rev

#DB_LOC = os.path.normpath('c:\\Users\\Vincent S\\game-revenant\\shadows\\shadows_twitter_analysis.sqlite')
DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')


GAME_REV_FOLLOWERS = """ CREATE TABLE IF NOT EXISTS game_rev_followers (
                            id BIGINT PRIMARY KEY,
                            id_string TEXT NOT NULL,
                            name TEXT NOT NULL,
                            screen_name TEXT NOT NULL, 
                            location TEXT,
                            url TEXT,
                            description TEXT, 
                            protected INTEGER,
                            verified INTEGER,
                            followers_count INTEGER,
                            friend_count INTEGER,
                            listed_count INTEGER,
                            favourites_count INTEGER,
                            statuses_count INTEGER,
                            created_at TEXT,
                            default_profile TEXT,
                            default_profile_image TEXT                            
                            ); """ 

SCREEN_NAME = 'gamerevenant'

conn = create_connection(DB_LOC)
create_table(conn, GAME_REV_FOLLOWERS)

rows_added = 0

for flwrs in tweepy.Cursor(api.followers, SCREEN_NAME).pages():
    # get followers profile info 
    new_rows = pull_user_data(flwrs) 
    # add follower info to SQL data base
    add_follower_game_rev(conn, new_rows)
    conn.commit()
    # print out status report
    rows_added += len(new_rows)
    print(str(rows_added) + ' follower profiles have been added to game_rev_followers')
    sleep(60)
    
conn.close()


# %% sqlite us two (monument valley)

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_follower_ustwo

DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')

USTWO_FOLLOWERS = """ CREATE TABLE IF NOT EXISTS ustwo_followers (
                            id BIGINT PRIMARY KEY,
                            id_string TEXT NOT NULL,
                            name TEXT NOT NULL,
                            screen_name TEXT NOT NULL, 
                            location TEXT,
                            url TEXT,
                            description TEXT, 
                            protected INTEGER,
                            verified INTEGER,
                            followers_count INTEGER,
                            friend_count INTEGER,
                            listed_count INTEGER,
                            favourites_count INTEGER,
                            statuses_count INTEGER,
                            created_at TEXT,
                            default_profile TEXT,
                            default_profile_image TEXT                            
                            ); """ 

SCREEN_NAME = 'ustwogames'

conn = create_connection(DB_LOC)
create_table(conn, USTWO_FOLLOWERS)

rows_added = 0
#tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME).pages()
# if restarting from point where mining stopped, call teh following:
tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME, cursor=current_cursor).pages()

for flwrs in tweepy_cursor:
    #get current cursor position in case of crash or exception
    current_cursor = tweepy_cursor.next_cursor
    # get followers profile info 
    new_rows = pull_user_data(flwrs) 
    # add follower info to SQL data base
    add_follower_ustwo(conn, new_rows)
    conn.commit()
    # print out status report
    rows_added += len(new_rows)
    print(str(rows_added) + ' follower profiles have been added to ustwo_followers')
    print('current cursor location = ' + str(current_cursor))
    sleep(60)

conn.close()


# %% sqlite Playdead (Limbo)

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_follower_playdead

DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')

PLAYDEAD = """ CREATE TABLE IF NOT EXISTS playdead_followers (
                            id BIGINT PRIMARY KEY,
                            id_string TEXT NOT NULL,
                            name TEXT NOT NULL,
                            screen_name TEXT NOT NULL, 
                            location TEXT,
                            url TEXT,
                            description TEXT, 
                            protected INTEGER,
                            verified INTEGER,
                            followers_count INTEGER,
                            friend_count INTEGER,
                            listed_count INTEGER,
                            favourites_count INTEGER,
                            statuses_count INTEGER,
                            created_at TEXT,
                            default_profile TEXT,
                            default_profile_image TEXT                            
                            ); """ 

SCREEN_NAME = 'Playdead'

conn = create_connection(DB_LOC)
create_table(conn, PLAYDEAD)

rows_added = 0
tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME).pages()
# if restarting from point where mining stopped, call teh following:
#tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME, cursor=current_cursor).pages()

for flwrs in tweepy_cursor:
    #get current cursor position in case of crash or exception
    current_cursor = tweepy_cursor.next_cursor
    # get followers profile info 
    new_rows = pull_user_data(flwrs) 
    # add follower info to SQL data base
    add_follower_playdead(conn, new_rows)
    conn.commit()
    # print out status report
    rows_added += len(new_rows)
    print(str(rows_added) + ' follower profiles have been added to playdead_followers')
    print('current cursor location = ' + str(current_cursor))
    sleep(60)

conn.close()

# %% sqlite That Game Compnay (Journey)

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_follower_that_game_comp

DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')

THAT_GAME_COMP = """ CREATE TABLE IF NOT EXISTS that_game_comp_followers (
                            id BIGINT PRIMARY KEY,
                            id_string TEXT NOT NULL,
                            name TEXT NOT NULL,
                            screen_name TEXT NOT NULL, 
                            location TEXT,
                            url TEXT,
                            description TEXT, 
                            protected INTEGER,
                            verified INTEGER,
                            followers_count INTEGER,
                            friend_count INTEGER,
                            listed_count INTEGER,
                            favourites_count INTEGER,
                            statuses_count INTEGER,
                            created_at TEXT,
                            default_profile TEXT,
                            default_profile_image TEXT                            
                            ); """ 

SCREEN_NAME = 'thatgamecompany'

conn = create_connection(DB_LOC)
create_table(conn, THAT_GAME_COMP)

rows_added = 0
tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME).pages()
# if restarting from point where mining stopped, call teh following:
tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME, cursor=current_cursor).pages()

for flwrs in tweepy_cursor:
    #get current cursor position in case of crash or exception
    current_cursor = tweepy_cursor.next_cursor
    # get followers profile info 
    new_rows = pull_user_data(flwrs) 
    # add follower info to SQL data base
    add_follower_that_game_comp(conn, new_rows)
    conn.commit()
    # print out status report
    rows_added += len(new_rows)
    print(str(rows_added) + ' follower profiles have been added to that_game_comp_followers')
    print('current cursor location = ' + str(current_cursor))
    sleep(60)

conn.close()

# %% sqlite Rusty Lake

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_follower_rusty_lake

DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')

RUSTY_LAKE = """ CREATE TABLE IF NOT EXISTS rusty_lake_followers (
                            id BIGINT PRIMARY KEY,
                            id_string TEXT NOT NULL,
                            name TEXT NOT NULL,
                            screen_name TEXT NOT NULL, 
                            location TEXT,
                            url TEXT,
                            description TEXT, 
                            protected INTEGER,
                            verified INTEGER,
                            followers_count INTEGER,
                            friend_count INTEGER,
                            listed_count INTEGER,
                            favourites_count INTEGER,
                            statuses_count INTEGER,
                            created_at TEXT,
                            default_profile TEXT,
                            default_profile_image TEXT                            
                            ); """ 

SCREEN_NAME = 'rustylakecom'

conn = create_connection(DB_LOC)
create_table(conn, RUSTY_LAKE)

rows_added = 0
tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME).pages()
# if restarting from point where mining stopped, call teh following:
tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME, cursor=current_cursor).pages()

for flwrs in tweepy_cursor:
    #get current cursor position in case of crash or exception
    current_cursor = tweepy_cursor.next_cursor
    # get followers profile info 
    new_rows = pull_user_data(flwrs) 
    # add follower info to SQL data base
    add_follower_rusty_lake(conn, new_rows)
    conn.commit()
    # print out status report
    rows_added += len(new_rows)
    print(str(rows_added) + ' follower profiles have been added to rusty_lake_followers')
    print('current cursor location = ' + str(current_cursor))
    sleep(60)

conn.close()
# %% Retrieve just the IDs of USTWO followers

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_follower_ids_ustwo

# pulls follower ids
SCREEN_NAME = 'ustwogames'
all_ids = []

for flwrs in tweepy.Cursor(api.followers_ids, SCREEN_NAME).pages():
    # add list of 5000 follower ids
    all_ids.extend(flwrs) 
    # print out status report
    print(str(len(all_ids)) + ' follower ids have been collected')
    sleep(30)

#add ids to SQL database
DB_LOC = os.path.normpath('c:\\Users\\Vincent S\\game-revenant\\shadows\\shadows_twitter_analysis.sqlite')

USTWO_FOLLOWERS_IDS = """ CREATE TABLE IF NOT EXISTS ustwo_followers_ids (
                            id BIGINT PRIMARY KEY                          
                            ); """ 

conn = create_connection(DB_LOC)
create_table(conn, USTWO_FOLLOWERS_IDS)

add_follower_ids_ustwo(conn, list(zip(all_ids)))

conn.commit()
conn.close()

# %% Retrieve IDs of the friends of Game Rev followers

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_friends_ids_game_rev

# connect to DB
#DB_LOC = os.path.normpath('c:\\Users\\Vincent S\\game-revenant\\shadows\\shadows_twitter_analysis.sqlite')
DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')

GAME_REV_FRIENDS_IDS = """ CREATE TABLE IF NOT EXISTS game_rev_friends_ids (
                            user_id BIGINT,
                            friend_id BIGINT
                            ); """ 

conn = create_connection(DB_LOC)
create_table(conn, GAME_REV_FRIENDS_IDS)

# get profile info from GameRevenant followers
gr_fol = pd.read_csv('game_rev_followers.csv')

SCREEN_NAME = 'GameRevenant'

# if restarting from point where mining stopped, call teh following:
#tweepy_cursor = tweepy.Cursor(api.followers, SCREEN_NAME, cursor=current_cursor).pages()

cnt_users_processed = 126
# NOTE THAT WE ARE ITERATING ONLY THORUGH PART OF LIST DUE TO CRASH
for id_int in gr_fol['id'][cnt_users_processed:]:
    
    tweepy_cursor = tweepy.Cursor(api.friends_ids, id_int).pages()
    
    frnds_ids = []
    
    # if the twitter profile is protected, can't pull user's friends
    if gr_fol.loc[gr_fol['id']==id_int]['protected'].item():
        print('User ' + str(id_int) + ' is a protected account. Skipping...')
        continue
    else:
        while True:
            try:
                frnds = tweepy_cursor.next()
                #get current cursor position in case of crash or exception
                current_cursor = tweepy_cursor.next_cursor
                # add list of 5000 follower ids
                frnds_ids.extend(frnds) 
                # print out status report
                print(str(len(frnds_ids)) + 
                      ' friend ids have been collected from the user ' + str(id_int))
                sleep(60)
#           except tweepy.TweepError:
#               print('Over the API limit! Waiting 15 min')
#               sleep(15*60)
#               continue
            except StopIteration:
                break
    
        # col 1: follower id; col 2: ids of his/her friends
        new_rows = list(zip([id_int]*len(frnds_ids), frnds_ids))
        add_friends_ids_game_rev(conn, new_rows)
        conn.commit()
    
    cnt_users_processed += 1
    print('User ' + str(id_int) + ' friends added. ' + 
          str(cnt_users_processed) + ' users mined')
    
conn.close()

# %% Retrieve friend profiles of GR followers, in order of most popular

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_gr_fol_friend

#DB_LOC = os.path.normpath('c:\\Users\\Vincent S\\game-revenant\\shadows\\shadows_twitter_analysis.sqlite')
DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')


GAME_REV_FOL_FRIENDS = """ CREATE TABLE IF NOT EXISTS game_rev_fol_friends (
                            id BIGINT PRIMARY KEY,
                            id_string TEXT NOT NULL,
                            name TEXT NOT NULL,
                            screen_name TEXT NOT NULL, 
                            location TEXT,
                            url TEXT,
                            description TEXT, 
                            protected INTEGER,
                            verified INTEGER,
                            followers_count INTEGER,
                            friend_count INTEGER,
                            listed_count INTEGER,
                            favourites_count INTEGER,
                            statuses_count INTEGER,
                            created_at TEXT,
                            default_profile TEXT,
                            default_profile_image TEXT,
                            popularity_count INTEGER
                            ); """ 


conn = create_connection(DB_LOC)
create_table(conn, GAME_REV_FOL_FRIENDS)

# pull list of friend ids of GR followers
gr_fol_frnds = pd.read_csv('game_rev_friends_ids.csv')

# generate list of other users GR followers are friends with, in order of popularity among GR followers
frnds_pop = gr_fol_frnds['friend_id'].value_counts().to_dict()

for frnd in frnds_pop:
    # get friend profile info
    user_prof = pull_user_data(api.get_user(frnd))
    # add additional column: number of other followers that are also friends with this user
    user_prof.append(frnds_pop[frnd])
    # add profile info to SQL db
    add_gr_fol_friend(conn, user_prof)
    conn.commit()
    # status report
    print('User ' + str(frnd) + ' added to DB. ' + str(frnds_pop[frnd]) + 
          ' other Game Rev followers are friends with this user')
    sleep(1) #limit to 900 calls/15 min window
    
conn.close()


    
# %% Retrieve IDs of followers of USTWO game cluster sample

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_friends_ustwo_game_clust

# connect to DB
#DB_LOC = os.path.normpath('c:\\Users\\Vincent S\\game-revenant\\shadows\\shadows_twitter_analysis.sqlite')
DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')

USTWO_GAME_CLUST_FRIENDS_IDS = """ CREATE TABLE IF NOT EXISTS ustwo_game_clust_friends_ids (
                            user_id BIGINT,
                            friend_id BIGINT
                            ); """ 

conn = create_connection(DB_LOC)
create_table(conn, USTWO_GAME_CLUST_FRIENDS_IDS)

# get profile info from GameRevenant followers
df = pd.read_csv('dbscan_game_cluster_sample.csv')

cnt_users_processed = 34 
# NOTE THAT WE ARE ITERATING ONLY THORUGH PART OF LIST DO CRASH
for id_int in df['id'][cnt_users_processed:]:
    
    tweepy_cursor = tweepy.Cursor(api.friends_ids, id_int).pages()
    
    frnds_ids = []
    
    # if the twitter profile is protected, can't pull user's friends
    if df.loc[df['id']==id_int]['protected'].item():
        print('User ' + str(id_int) + ' is a protected account. Skipping...')
        continue
    else:
        while True:
            try:
                frnds = tweepy_cursor.next()
                #get current cursor position in case of crash or exception
                current_cursor = tweepy_cursor.next_cursor
                # add list of 5000 follower ids
                frnds_ids.extend(frnds) 
                # print out status report
                print(str(len(frnds_ids)) + 
                      ' friend ids have been collected from the user ' + str(id_int))
                sleep(60)
            except tweepy.TweepError:
                print('TweepError; skipping account...')
                print(str(cnt_users_processed) + ' users mined')
                sleep(60)
                cnt_users_processed += 1
                break
            except StopIteration:
                break
    
        # col 1: follower id; col 2: ids of his/her friends
        new_rows = list(zip([id_int]*len(frnds_ids), frnds_ids))
        add_friends_ustwo_game_clust(conn, new_rows)
        conn.commit()
    
    cnt_users_processed += 1
    print('User ' + str(id_int) + ' friends added. ' + 
          str(cnt_users_processed) + ' users mined')
    
conn.close()


# %% Retrieve friend profiles of USTWO game cluster followers, in order of most popular

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_ustwo_game_clust_fol_friend
import itertools

#DB_LOC = os.path.normpath('c:\\Users\\Vincent S\\game-revenant\\shadows\\shadows_twitter_analysis.sqlite')
DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')


USTWO_GAME_CLUST_FOL_FRIENDS = """ CREATE TABLE IF NOT EXISTS ustwo_game_clust_fol_friends (
                            id BIGINT PRIMARY KEY,
                            id_string TEXT NOT NULL,
                            name TEXT NOT NULL,
                            screen_name TEXT NOT NULL, 
                            location TEXT,
                            url TEXT,
                            description TEXT, 
                            protected INTEGER,
                            verified INTEGER,
                            followers_count INTEGER,
                            friend_count INTEGER,
                            listed_count INTEGER,
                            favourites_count INTEGER,
                            statuses_count INTEGER,
                            created_at TEXT,
                            default_profile TEXT,
                            default_profile_image TEXT,
                            popularity_count INTEGER
                            ); """ 


conn = create_connection(DB_LOC)
create_table(conn, USTWO_GAME_CLUST_FOL_FRIENDS)

# pull list of friend ids of GR followers
ustwo_fol_frnds = pd.read_csv('ustwo_game_clust_friends_ids.csv')

# generate list of other users GR followers are friends with, in order of popularity among GR followers
cnt_users_processed = 4929 

frnds_pop_all = ustwo_fol_frnds['friend_id'].value_counts().to_dict()
frnds_pop = dict(itertools.islice(frnds_pop_all.items(), cnt_users_processed, None))

for frnd in frnds_pop:

    try:
        # get friend profile info
        user_prof = pull_user_data(api.get_user(frnd))
        # add additional column: number of other followers that are also friends with this user
        user_prof.append(frnds_pop[frnd])
        # add profile info to SQL db
        add_ustwo_game_clust_fol_friend(conn, user_prof)
        conn.commit()
        # status report
        print('User ' + str(frnd) + ' added to DB. ' + str(frnds_pop[frnd]) + 
              ' other USTWO game cluster followers are friends with this user')
        sleep(1.25) #limit to 900 calls/15 min window
    except tweepy.TweepError:
        print('TweepError; skipping account...')
        sleep(1.25)
        continue
    
conn.close()


# %% Retrieve IDs of followers of sampled (all) USTWO followers

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_friends_ustwo_sampled

# connect to DB
#DB_LOC = os.path.normpath('c:\\Users\\Vincent S\\game-revenant\\shadows\\shadows_twitter_analysis.sqlite')
DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')

USTWO_SAMPLED_FRIENDS_IDS = """ CREATE TABLE IF NOT EXISTS ustwo_sampled_friends_ids (
                            user_id BIGINT,
                            friend_id BIGINT
                            ); """ 

conn = create_connection(DB_LOC)
create_table(conn, USTWO_SAMPLED_FRIENDS_IDS)

# get profile info from GameRevenant followers
df = pd.read_csv('sampled_ustwo_followers_frac-10.csv')

cnt_users_processed = 0 
# NOTE THAT WE ARE ITERATING ONLY THORUGH PART OF LIST DO CRASH
for id_int in df['id'][cnt_users_processed:]:
    
    tweepy_cursor = tweepy.Cursor(api.friends_ids, id_int).pages()
    
    frnds_ids = []
    
    # if the twitter profile is protected, can't pull user's friends
    if df.loc[df['id']==id_int]['protected'].item():
        print('User ' + str(id_int) + ' is a protected account. Skipping...')
        continue
    else:
        while True:
            try:
                frnds = tweepy_cursor.next()
                #get current cursor position in case of crash or exception
                current_cursor = tweepy_cursor.next_cursor
                # add list of 5000 follower ids
                frnds_ids.extend(frnds) 
                # print out status report
                print(str(len(frnds_ids)) + 
                      ' friend ids have been collected from the user ' + str(id_int))
                sleep(60)
            except tweepy.TweepError:
                print('TweepError; skipping account...')
                print(str(cnt_users_processed) + ' users mined')
                sleep(60)
                cnt_users_processed += 1
                break
            except StopIteration:
                break
    
        # col 1: follower id; col 2: ids of his/her friends
        new_rows = list(zip([id_int]*len(frnds_ids), frnds_ids))
        add_friends_ustwo_sampled(conn, new_rows)
        conn.commit()
    
    cnt_users_processed += 1
    print('User ' + str(id_int) + ' friends added. ' + 
          str(cnt_users_processed) + ' users mined')
    
conn.close()

# %% Retrieve friend profiles of USTWO sampled followers, in order of most popular

from sqlite_fx import create_connection
from sqlite_fx import create_table
from sqlite_fx import add_ustwo_sampled_fol_friend
import itertools

#DB_LOC = os.path.normpath('c:\\Users\\Vincent S\\game-revenant\\shadows\\shadows_twitter_analysis.sqlite')
DB_LOC = os.path.normpath('c:\\Users\\Vincent\\Game-Revenant\\Shadows\\shadows_twitter_analysis.sqlite')


USTWO_SAMPLED_FOL_FRIENDS = """ CREATE TABLE IF NOT EXISTS ustwo_sampled_fol_friends (
                            id BIGINT PRIMARY KEY,
                            id_string TEXT NOT NULL,
                            name TEXT NOT NULL,
                            screen_name TEXT NOT NULL, 
                            location TEXT,
                            url TEXT,
                            description TEXT, 
                            protected INTEGER,
                            verified INTEGER,
                            followers_count INTEGER,
                            friend_count INTEGER,
                            listed_count INTEGER,
                            favourites_count INTEGER,
                            statuses_count INTEGER,
                            created_at TEXT,
                            default_profile TEXT,
                            default_profile_image TEXT,
                            popularity_count INTEGER
                            ); """ 


conn = create_connection(DB_LOC)
create_table(conn, USTWO_SAMPLED_FOL_FRIENDS)

# pull list of friend ids of GR followers
ustwo_fol_frnds = pd.read_csv('ustwo_sampled_friends_ids.csv')

# generate list of other users GR followers are friends with, in order of popularity among GR followers
cnt_users_processed = 0 

frnds_pop_all = ustwo_fol_frnds['friend_id'].value_counts().to_dict()
frnds_pop = dict(itertools.islice(frnds_pop_all.items(), cnt_users_processed, None))

for frnd in frnds_pop:

    try:
        # get friend profile info
        user_prof = pull_user_data(api.get_user(frnd))
        # add additional column: number of other followers that are also friends with this user
        user_prof.append(frnds_pop[frnd])
        # add profile info to SQL db
        add_ustwo_sampled_fol_friend(conn, user_prof)
        conn.commit()
        # status report
        print('User ' + str(frnd) + ' added to DB. ' + str(frnds_pop[frnd]) + 
              ' other USTWO sampled followers are friends with this user')
        sleep(1.25) #limit to 900 calls/15 min window
    except tweepy.TweepError:
        print('TweepError; skipping account...')
        sleep(1.25)
        continue
    
conn.close()
