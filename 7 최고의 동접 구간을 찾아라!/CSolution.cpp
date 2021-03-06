// CSolution.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <iomanip>

using namespace std;

string make_two(int time) {
	stringstream ss;

	if (time < 10) {
		ss << "0" << time;
	}
	else {
		ss << time;
	}
	return ss.str();
}

string make_print(int time) {
	stringstream ss;

	ss << (int)(time / 60) << ":" << make_two(time % 60);
	return ss.str();
}

int main()
{
	int count, h, m, T_Stime, T_Etime;
	string start, end;

	int t_table[24 * 60] = { 0 };

	cin >> count;
	
	for (int _loop = 0; _loop < count; _loop++) {
		cin >> start >> end;

		h = stoi(start.substr(0, 2));
		m = stoi(start.substr(3, 5));

		T_Stime = h * 60 + m;

		h = stoi(end.substr(0, 2));
		m = stoi(end.substr(3, 5));

		T_Etime = h * 60 + m;

		for (int _idx = T_Stime; _idx < T_Etime; _idx++) {
			t_table[_idx] += 1;
		}
	}

	int _max = *max_element(t_table, t_table + sizeof(t_table) / sizeof(int)),
		_start = distance(t_table, max_element(t_table, t_table + sizeof(t_table) / sizeof(int)));
	
	
	int _temp = -1, _idx = 0;

	for (_idx = _start; _idx < sizeof(t_table) / sizeof(int); _idx++) {
		_temp = t_table[_idx];

		if (_temp < _max) {
			break;
		}
	}

	cout << _max << endl;
	cout << make_print(_start) << " " << make_print(_idx) << endl;

    return 0;
}
