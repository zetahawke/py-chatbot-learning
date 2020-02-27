# frozen_string_literal: true

p "Hello there.\n
  I'm a ruby terminal chatbot that uses python's chatterbot library to delegate all AI/ML tasks.\n
  My only porpuses is to comunicate this through ruby inputs... lol :D
  "

loop do
  text_to_pass_through = gets.chomp
  result = `python chatbot.py "#{text_to_pass_through}"`
  p result
rescue StandardError => _e
  break
end
