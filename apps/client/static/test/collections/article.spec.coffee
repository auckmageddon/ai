# global describe, beforeEach, assert, it
"use strict"

describe 'Article Collection', ->
  beforeEach ->
    @Article = new client.Collections.ArticleCollection()
