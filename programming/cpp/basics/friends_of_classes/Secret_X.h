class Secret_X
{
	private:
		int x;
	public:
		void init_X(int);
		Secret_X();
		~Secret_X();
	friend int read_x(Secret_X);
};
