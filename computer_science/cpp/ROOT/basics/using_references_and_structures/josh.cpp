struct Jet
{
	TVector3 p;
	double energy;
	double thrust;
	double discriminant;
	double phi;
	double n_positive_pt_weighted;
	double n_negative_pt_weighted;
	double n_neutral_pt_weighted;
	int n;

	void clear() 
	{ 
		p.Clear();
		phi = -999.0;
		energy = -999.0;
		thrust = -999.0;
		discriminant = -999.0
			n_positive_pt_weighted 0.0;
		n_negative_pt_weighted 0.0;
		n_neutral_pt_weighted = 0.0;
		n = -999;
	}
};

void RunJets()
{
	std::vector<Jet> *jets = 0; // (this is above in the code)
	std::vector<Jet> jets_obj;

	cout << endl;
	cout << "   &jets->front(): " << &jets->front() << ", &jets->end():" << &jets->end() << endl;
	for (unsigned jet_i = 0; jet_i < jets->size(); jet_i++) 
	{
		cout << "   &(jets->at(" << jet_i << ")): " << &(jets->at(jet_i)) << ", jets->at(" << jet_i << ").phi: " << jets->at(jet_i).phi << endl;
		jets_obj.push_back(jets->at(jet_i));
	}

	for (unsigned jet_i = 0; jet_i < jets_obj.size(); jet_i++) 
	{
		cout << "&(jets_obj.at(" << jet_i << ")): " << &(jets_obj.at(jet_i)) << ", jets_obj.at(" << jet_i << ").phi: " << jets_obj.at(jet_i).phi << endl;
	}

	std::vector<Jet>::iterator iter;
	iter = jets_obj->begin();
	cout << "          &(iter): " << &(iter) << endl;// << ", iter->phi: " << iter.phi << endl;
}
