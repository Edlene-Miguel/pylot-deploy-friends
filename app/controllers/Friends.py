from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)

        self.load_model('Friend')

   
    def index(self):
        friends = self.models['Friend'].get_all_friends()
        return self.load_view('index.html', friends = friends)

    def new(self):
        
        return self.load_view('new.html')

    def create(self):

        friend = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'occupation' : request.form['occupation'],
            'known_for' : request.form['known_for']
        }
        self.models['Friend'].create_friend(friend)
        return redirect('/')

    def show(self, id):

        friend = self.models['Friend'].get_friend_by_id(id)
        return self.load_view('show.html', friend = friend)

    def edit(self, id):

        friend = self.models['Friend'].get_friend_by_id(id)
        return self.load_view('edit.html', friend = friend)

    def update(self, id):

        friend = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'occupation' : request.form['occupation'],
            'known_for' : request.form['known_for']
        }
        self.models['Friend'].update(id, friend)
        return redirect('/')

    def deletepage(self, id):
        friend = self.models['Friend'].get_friend_by_id(id)
        print friend
        return self.load_view('delete.html', friend = friend)

    def delete(self, id):

        self.models['Friend'].delete(id)
        return redirect('/')

