var RIGHT = "right";
var LEFT = "left";
var UP = "up";
var DOWN = "down";
X_AXIS = "x";
Y_AXIS = "Y";
var ViewPort = function (netX, netY) {
	this.obj_data = [];
	this.pin = -1;
	this.disabled = false;
	this.netX = netX;
	this.netY = netY;
};
ViewPort.prototype.addObj = function (x_pos_r, y_pos_r, direction) {
	this.obj_data.push([x_pos_r, y_pos_r, direction]);
	this.pin += 1;
	return [this.pin, [x_pos_r, y_pos_r]];
};
ViewPort.prototype.setDirection = function (new_direction) {
	var a = 0;
	while (a <= this.obj_data.length-1) {
		this.obj_data[a][2] = new_direction;
		a++;
	}
	return new_direction;
};
ViewPort.prototype.stopMotion = function () {
	var a = 0;
	while (a <= this.obj_data.length-1) {
		this.obj_data[a][2] = null;
		a++;
	}
	return "Motion had been stopped";
};
ViewPort.prototype.getX = function (pin) {
	return this.obj_data[pin][0];
};
ViewPort.prototype.getY = function (pin) {
	return this.obj_data[pin][1];
};
ViewPort.prototype.getNetX = function () {
	return this.netX;
};
ViewPort.prototype.getNetY = function () {
	return this.netY;
};
ViewPort.prototype.setX = function (pin, new_x) {
	this.obj_data[pin][0] = new_x;
	return this.obj_data[pin][0];
};
ViewPort.prototype.setY = function (pin, new_y) {
	this.obj_data[pin][1] = new_y;
	return this.obj_data[pin][1];
};
ViewPort.prototype.getDirection = function() {
	return this.obj_data[0][2];
};
ViewPort.prototype.disable  = function () {
	this.disabled = true;
};
ViewPort.prototype.enable = function () {
	this.disabled = false;
};
ViewPort.prototype.getCords = function (pin) {
	return [this.obj_data[pin][0], this.obj_data[pin][1]]
};
ViewPort.prototype.setCords = function (pin, newCords) {
	this.obj_data[pin][0] = newCords[0];
	this.obj_data[pin][1] = newCords[1];
};
ViewPort.prototype.updateStats = function (by) {
	if (this.disabled == false) {
		if (this.obj_data[0][2] == "right") {
			this.netX += by;
			var a = 0;
			while (a <= this.obj_data.length-1) {
				this.obj_data[a][0] -= by;
				a++;
			}
		} else if (this.obj_data[0][2] == "left") {
			this.netX -= by;
			var a = 0;
			while (a <= this.obj_data.length-1) {
				this.obj_data[a][0] += by;
				a++;
			}
		} else if (this.obj_data[0][2] == "up") {
			this.netY -= by;
			var a = 0;
			while (a <= this.obj_data.length-1) {
				this.obj_data[a][1] += by;
				a++;
			}
		} else if (this.obj_data[0][2] == "down") {
			this.netY += by;
			var a = 0;
			while (a <= this.obj_data.length-1) {
				this.obj_data[a][1] -= by;
				a++;
			}
		}
	}
};
ViewPort.prototype.updateCustomStats = function (pin, by) {
	if (this.disabled == false) {
		if (this.obj_data[0][2] == "right") {
			this.obj_data[pin][0] -= by;
		} else if (this.obj_data[pin][2] == "left") {
			this.obj_data[pin][0] += by;
		} else if (this.obj_data[pin][2] == "up") {
			this.obj_data[pin][1] += by;
		} else if (this.obj_data[pin][2] == "down") {
			this.obj_data[pin][1] -= by;
		}
	}
};
var VIEW = {"ViewPort": ViewPort, "RIGHT":"right", "LEFT":"left", "UP":"up", "DOWN":"down", "REVISION": "View.js v2.0"};
console.log("%c" + VIEW.REVISION, 'color:#00aaff; background-color:black; font-size:30px; font-family:sans-serif;line-height:1.15;');