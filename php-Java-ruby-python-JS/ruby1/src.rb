def constant_expression(val)
	z() if ~(s == 0)  # A CONSTANT_EXPRESSION_RESULT here. '!(s == 0)' is intended.
end


def deadcode(obj)
	if (obj.nil?)
		return 1
	end
	somethingElse()
	if (obj == nil)
		return 2  # Defect: dead code
	end
	3
end


def call_on_inferred_nil(x)
	if not x
		puts "x is nil or false on this path."
	end
	# On one of two paths reaching here, x is nil or false.
	# Invoking 'respond_to?' on x is OK because it is 
	# part of the well-known NilClass interface.
	return 'FAIL' if not x.respond_to? :is_a?  # No defect here.

	# But invoking 'call' causes a defect because it is not well-known.
	x.call()  # Defect here.
end


def unreachable_to_fix(cond, message)
	if (cond)
		raise RuntimeError, message
		log("Fatal error: " + message) # Defect here.
	end
end

def unreachable_to_fix_v1(cond, message)
	if (cond)
		raise RuntimeError, message
		log("Fatal error: 2" + message) # Defect here.
	end
end

def identical_branches(a, b, op)
	if op == '+' # IDENTICAL_BRANCHES defect
		a + b
	else
		a + b
	end
end

def no_effect()
	assert(Math::PI > 3.14)
	assert(Math::PI < 3.15)
	Math::E > 2.71           # Defect
	assert(Math::E < 2.72)
end
