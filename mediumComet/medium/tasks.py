from django.template.loader import render_to_string
from django.core import mail
import json
from collections import Set
from mediumComet import settings
from .models import Post, Topics
from celery import task
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from preferences import preferences
import os
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import localtime
import requests
import time
import logging

logger = logging.getLogger()


#run from medium.tasks import scrape_medium
# scrape_medium.run()
@task
def scrape_medium():

    import time

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    browser = webdriver.Chrome('/usr/local/bin/chromedriver')

    browser.get("https://medium.com/topic/business")
    business_topic = Topics.objects.create(
        url='https://medium.com/topic/business', name='business')

    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")

    no_of_pagedowns = 20

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns -= 1

    post_elems_links = browser.find_elements_by_xpath(
        "//div[@class='eb c aq ec ab' and 1]/div[@class='ed ee' and 1]/h3[@class='ch x ci bh cj bi ef eg eh c al ei ej' and 1]/a['href'][1]"
    )
    post_elems_titles = browser.find_elements_by_xpath(
        "//section[@class='n o p dy r c']/div[@class='p dz' and 1]/section[@class='dw dx t' and 1]/div[@class='m r t cz ea' and 1]/div[@class='eb c aq ec ab' and 1]/div[@class='ed ee' and 1]/h3[@class='ch x ci bh cj bi ef eg eh c al ei ej' and 1]"
    )
    post_elems_creator = browser.find_elements_by_xpath(
        "//section[@class='n o p dy r c']/div[@class='p dz' and 1]/section[@class='dw dx t' and 1]/div[@class='m r t cz ea' and 1]/div[@class='cn eb c aq ec ab' and 2]/div[@class='t' and 1]/div[@class='ep t ea' and 1]/a[1]/span[@class='bh b bi bj bk bl c ch x' and 1]"
    )
    post_elems_details = browser.find_elements_by_xpath(
        "//section[@class='n o p dy r c']/div[@class='p dz' and 1]/section[@class='dw dx t' and 1]/div[@class='m r t cz ea' and 1]/div[@class='cn eb c aq ec ab' and 2]/div[@class='t' and 1]/div[@class='ep t ea' and 1]/div[@class='eq c' and 1]/span[@class='bh b bi bj bk bl c bm bn' and 1]"
    )
    print(post_elems_creator)
    for post_link, post_title, post_creator, post_detail in zip(
            post_elems_links, post_elems_titles, post_elems_creator,
            post_elems_details):

        print(post_title.text)
        print(post_creator.text)
        print(post_detail.text)
        print(post_link.get_attribute('href'))

        Post.objects.create(
            url=post_link.get_attribute('href'),
            title=post_title.text,
            author=post_creator.text,
            details=post_detail.text,
            topic=business_topic)
