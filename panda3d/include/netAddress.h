// Filename: netAddress.h
// Created by:  drose (08Feb00)
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

#ifndef NETADDRESS_H
#define NETADDRESS_H

#include "pandabase.h"
#include "numeric_types.h"
#include "socket_address.h"

////////////////////////////////////////////////////////////////////
//       Class : NetAddress
// Description : Represents a network address to which UDP packets may
//               be sent or to which a TCP socket may be bound.
////////////////////////////////////////////////////////////////////
class EXPCL_PANDA_NET NetAddress {
PUBLISHED:
  NetAddress();
  NetAddress(const Socket_Address &addr);

  bool set_any(int port);
  bool set_localhost(int port);
  bool set_broadcast(int port);
  bool set_host(const string &hostname, int port);

  void clear();

  int get_port() const;
  void set_port(int port);
  string get_ip_string() const;
  PN_uint32 get_ip() const;
  PN_uint8 get_ip_component(int n) const;

  const Socket_Address &get_addr() const;

  void output(ostream &out) const;

  size_t get_hash() const;
  bool operator == (const NetAddress &other) const;
  bool operator != (const NetAddress &other) const;

private:
  Socket_Address _addr;
};

INLINE ostream &operator << (ostream &out, const NetAddress &addr) {
  addr.output(out);
  return out;
}

#endif

