Rails.application.routes.draw do
  get 'topics/new'
  get 'sessions/new'
  root 'pages#index'
  get 'pages/help'

  resources :users
  resources :topics

  get 'favorites/index'
  post '/favorites', to: 'favorites#create'
# 質問　resourses :favorites


  get '/login', to: 'sessions#new'
  post '/login', to: 'sessions#create'
  get '/logout', to: 'sessions#destroy'

end
