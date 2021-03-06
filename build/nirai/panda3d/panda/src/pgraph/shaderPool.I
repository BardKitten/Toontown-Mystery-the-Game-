// Filename: shaderPool.I
// Created by:  aignacio (Mar06)
//
////////////////////////////////////////////////////////////////////
//
// PANDA 3D SOFTWARE
// Copyright (c) Carnegie Mellon University.  All rights reserved.
//
// All use of this software is subject to the terms of the revised BSD
// license.  You should have received a copy of this license along
// with this source code in a file named "LICENSE."
//
////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::has_shader
//       Access: Public, Static
//  Description: Returns true if the shader has ever been loaded,
//               false otherwise.
////////////////////////////////////////////////////////////////////
INLINE bool ShaderPool::
has_shader(const Filename &filename) {
  return get_ptr()->ns_has_shader(filename);
}

////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::verify_shader
//       Access: Public, Static
//  Description: Loads the given filename up into a shader, if it has
//               not already been loaded, and returns true to indicate
//               success, or false to indicate failure.  If this
//               returns true, it is guaranteed that a subsequent call
//               to load_shader() with the same shader name will
//               return a valid Shader pointer.
////////////////////////////////////////////////////////////////////
INLINE bool ShaderPool::
verify_shader(const Filename &filename) {
  return load_shader(filename) != (Shader *)NULL;
}

////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::load_shader
//       Access: Public, Static
//  Description: Loads the given filename up into a shader, if it has
//               not already been loaded, and returns the new shader.
//               If a shader with the same filename was previously
//               loaded, returns that one instead.  If the shader
//               file cannot be found, returns NULL.
////////////////////////////////////////////////////////////////////
INLINE CPT(Shader) ShaderPool::
load_shader(const Filename &filename) {
  return get_ptr()->ns_load_shader(filename);
}

////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::add_shader
//       Access: Public, Static
//  Description: Adds the indicated already-loaded shader to the
//               pool.  The shader will always replace any
//               previously-loaded shader in the pool that had the
//               same filename.
////////////////////////////////////////////////////////////////////
INLINE void ShaderPool::
add_shader(const Filename &filename, Shader *shader) {
  get_ptr()->ns_add_shader(filename, shader);
}

////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::release_shader
//       Access: Public, Static
//  Description: Removes the indicated shader from the pool,
//               indicating it will never be loaded again; the shader
//               may then be freed.  If this function is never called,
//               a reference count will be maintained on every shader
//               every loaded, and shaders will never be freed.
////////////////////////////////////////////////////////////////////
INLINE void ShaderPool::
release_shader(const Filename &filename) {
  get_ptr()->ns_release_shader(filename);
}

////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::release_all_shaders
//       Access: Public, Static
//  Description: Releases all shaders in the pool and restores the
//               pool to the empty state.
////////////////////////////////////////////////////////////////////
INLINE void ShaderPool::
release_all_shaders() {
  get_ptr()->ns_release_all_shaders();
}

////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::garbage_collect
//       Access: Public, Static
//  Description: Releases only those shaders in the pool that have a
//               reference count of exactly 1; i.e. only those
//               shaders that are not being used outside of the pool.
//               Returns the number of shaders released.
////////////////////////////////////////////////////////////////////
INLINE int ShaderPool::
garbage_collect() {
  return get_ptr()->ns_garbage_collect();
}

////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::list_contents
//       Access: Public, Static
//  Description: Lists the contents of the shader pool to the
//               indicated output stream.
////////////////////////////////////////////////////////////////////
INLINE void ShaderPool::
list_contents(ostream &out) {
  get_ptr()->ns_list_contents(out);
}

////////////////////////////////////////////////////////////////////
//     Function: ShaderPool::Constructor
//       Access: Private
//  Description: The constructor is not intended to be called
//               directly; there's only supposed to be one ShaderPool
//               in the universe and it constructs itself.
////////////////////////////////////////////////////////////////////
INLINE ShaderPool::
ShaderPool() {
}
