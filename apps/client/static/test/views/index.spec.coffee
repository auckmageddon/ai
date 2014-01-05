# global describe, beforeEach, assert, it
"use strict"

describe 'Index View', ->
  beforeEach ->
    @Index = new client.Views.IndexView();
