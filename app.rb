require 'sinatra'
require 'rubygems'
require 'pony'

set :public, File.join(File.dirname(__FILE__), 'public')
set :views, File.join(File.dirname(__FILE__), 'views')

get '/' do
  erb :index
end

get '/home' do
  erb :index
end

get '/about' do
  erb :about
end

get '/contact' do
  erb :contact
end

get '/services' do
  erb :services
end

post '/contact' do
  name = params[:name]
  mail = params[:mail]
  body = params[:comments]
  address = params[:address]
  city = params[:city]
  state = params[:state]
  zipcode = params[:zipcode]
  telephone = params[:telephone]

  puts "#{body} \n \n #{address} \n #{city}, #{state} #{zipcode} \n #{telephone}"
  #flanzz@aol.com
  Pony.mail(:to => 'stolt45@gmail.com', :from => "#{mail}", :subject => "art inquiry from #{name}", :body => "#{body} \n \n #{address} \n #{city}, #{state} #{zipcode} \n #{telephone}")

  erb :contact
end
