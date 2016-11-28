#ifndef CYLINDER_H
#define CYLINDER_H
#define PI 3.1415
#include "body.h"

// Inherits public functions from body
class cylinder : public body
{
	protected:
		float radius;
		float height;
	public:
		virtual float GetVolume();
		virtual float GetSurface();
		cylinder (float, float);
		~cylinder() {};
};
#endif /* CYLINDER_H */
