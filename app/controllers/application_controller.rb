class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  add_flash_types :success, :info, :warning, :danger

  def current_user
    @current_user ||= User.find_by(id: session[:user_id])
  end

  def logged_in? #質問　ここの？と！について
    !current_user.nil?
  end

end
