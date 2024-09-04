#!/usr/bin/env ruby

# Check if exactly one argument is passed
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the input string
input = ARGV[0]

# Use a regular expression to find all occurrences of 'School'
matches = input.scan(/hbt+n/)

# Print the matches joined together
puts matches.join
