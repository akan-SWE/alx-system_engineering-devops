#!/usr/bin/env ruby
# match the case hbttn till hbttttttn
puts ARGV[0].scan(/hbt{2,5}n/).join
