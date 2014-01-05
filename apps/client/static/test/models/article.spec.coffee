# global describe, beforeEach, assert, it
"use strict"

describe 'Article Model', ->
  beforeEach ->
    @Article = new client.Models.ArticleModel();
