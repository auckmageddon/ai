# global describe, beforeEach, assert, it
"use strict"

describe 'Article View', ->
  beforeEach ->
    @Article = new client.Views.ArticleView();
