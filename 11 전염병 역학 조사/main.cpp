#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>

#define DEBUG 0

using namespace std;

vector<int> vec_mutual(vector<int> a, vector<int> b) {
	vector<int> result;
	result.resize(a.size() + b.size());
	auto itr = set_intersection(a.begin(), a.end(), b.begin(), b.end(), result.begin());
	result.erase(itr, result.end());

	return result;
}

vector<int> vec_merge(vector<int> a, vector<int> b) {
	vector<int> result;
	result.resize(a.size() + b.size());
	auto itr = set_union(a.begin(), a.end(), b.begin(), b.end(), result.begin());
	result.erase(itr, result.end());

	return result;
}

void print_1d_vector(vector<int> a) {
	for (int i = 0; i < a.size(); i++) {
		cout << a.at(i);
		if (i != a.size() - 1) cout << ", ";
	}
}

bool has_mutual(vector<int> a, vector<int> b) {
	return bool(vec_mutual(a, b).size());
}

int main() {
	// 인원 수, 만남 수
	int Cpersons, Cmeets;
	int x, y, c;
	cin >> Cpersons >> Cmeets;
	if (DEBUG)
		cout << "Person: " << Cpersons << ", Meets" << Cmeets << endl;

	// 전체 만남 벡터
	vector < vector < vector<int> > > meets(Cmeets);

	for (int i = 0; i < Cmeets; i++) {
		cin >> x >> y >> c;

		if (x > y) swap(x, y);

		vector<int> single_meet({ x,y });
		meets.at(c - 1).push_back(single_meet);
		if (DEBUG) cout << "VecPush at (" << c - 1 << ", " << meets.at(c - 1).size() - 1 << ")" << endl;
	}


	// 감염의심자 벡터 셋
	// 초기 1은 감염되었다고 간주
	vector<int> influ({ 1 });

	for (int i = 0; i < meets.size(); i++) {
		vector<int> temp(influ);
		for (int j = 0; j < meets.at(i).size(); j++) {
			if (has_mutual(influ, meets.at(i).at(j))) {
				temp = vec_merge(temp, meets.at(i).at(j));
			}
			if (DEBUG) {
				cout << "Report(" << i << "," << j << ") " << influ.size() << endl;
				cout << "    Vec(Temp) "; print_1d_vector(temp); cout << endl;
				cout << "    Vec(Influ) "; print_1d_vector(influ); cout << endl;
			}
		}
		if (DEBUG) cout << " * Vec Push Temp >> Influ  ...";
		influ = temp;
		if (DEBUG) cout << " Done!" << endl;
		temp.clear();
	}

	for (int i = 0; i < influ.size(); i++) {
		cout << influ.at(i);

		if (i != influ.size() - 1) {
			cout << " ";
		}
	}


	return 0;
}