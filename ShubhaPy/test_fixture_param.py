import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_fixture(DiffBrowsers):
    print(DiffBrowsers)


def test_fixture1(DiffBrowsers1):
    print(DiffBrowsers1)
    print("------")
    print(DiffBrowsers1[1])